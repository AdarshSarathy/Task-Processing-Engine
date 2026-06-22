from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import List

import models, schemas, crud
from database import SessionLocal, engine

# Initialize database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Processing API",
    description="A highly optimized RESTful API for task tracking and processing.",
    version="1.0.0"
)

# Dependency to safely handle DB sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    """
    Health check endpoint to verify API operation.
    """
    return RedirectResponse(url="/docs")

@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task for processing.
    """
    return crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve multiple tasks with pagination functionality.
    """
    return crud.get_tasks(db, skip=skip, limit=limit)

@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Retrieve specific task details by its unique identifier.
    """
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}/complete", response_model=schemas.Task)
def complete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Mark a specified task as completed.
    """
    db_task = crud.update_task_status(db, task_id=task_id, is_completed=True)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task completely from the system framework.
    """
    success = crud.delete_task(db, task_id=task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success", "message": "Task successfully deleted"}
