from sqlalchemy.orm import Session
import models, schemas

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False

def update_task_status(db: Session, task_id: int, is_completed: bool):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.is_completed = is_completed
        db.commit()
        db.refresh(db_task)
        return db_task
    return None
