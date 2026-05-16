from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from main import app, get_db
from database import Base
import models

# Set up test database to strictly isolate tests
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Override the database dependency to use the isolated test database
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def run_around_tests():
    # Setup: Ensure a clean slate before each test
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    yield
    # Teardown logic
    pass

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "operational", "service": "Task Processing API"}

def test_create_task():
    response = client.post(
        "/tasks/",
        json={"title": "Test Task", "description": "This is a test task"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert data["is_completed"] == False
    assert "id" in data

def test_read_tasks():
    # Create an initial task to verify reading lists
    client.post("/tasks/", json={"title": "Task 1"})
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_complete_task():
    post_res = client.post("/tasks/", json={"title": "Task to complete"})
    task_id = post_res.json()["id"]

    comp_res = client.put(f"/tasks/{task_id}/complete")
    assert comp_res.status_code == 200
    assert comp_res.json()["is_completed"] == True

def test_delete_task():
    post_res = client.post("/tasks/", json={"title": "Task to delete"})
    task_id = post_res.json()["id"]

    del_res = client.delete(f"/tasks/{task_id}")
    assert del_res.status_code == 200

    # Ensure it was securely deleted
    get_res = client.get(f"/tasks/{task_id}")
    assert get_res.status_code == 404
