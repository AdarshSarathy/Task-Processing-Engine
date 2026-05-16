from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Task Processing API",
    description="A highly optimized RESTful API for task tracking and processing.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """
    Health check endpoint to verify API operation.
    """
    return {"status": "operational", "service": "Task Processing API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
