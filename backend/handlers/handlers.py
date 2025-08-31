from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Query
from sqlalchemy.orm import Session
from backend.models import schemas
from backend.models import models
from backend.db import db as database
from backend.services.mail import send_email_notification

router = APIRouter(tags=["Tasks"])

@router.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=201,
    responses={
        201: {"description": "Task created"},
        400: {"description": "Invalid input"}
    }
)
def create_task(
    task: schemas.TaskCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(database.get_db)
):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    
    background_tasks.add_task(send_email_notification, db_task)
    return db_task

@router.get("/tasks", response_model=list[schemas.TaskResponse])
def read_tasks(
    completed: bool | None = Query(None, description="Фильтр по статусу выполнения"),
    limit: int = Query(10, gt=0, le=100, description="Лимит результатов"),
    db: Session = Depends(database.get_db)
):
    query = db.query(models.Task)
    if completed is not None:
        query = query.filter(models.Task.completed == completed)
    return query.limit(limit).all()

@router.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(database.get_db)
):
    db_task = db.query(models.Task).get(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    
    db.commit()
    return db_task

@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(
    task_id: int,
    db: Session = Depends(database.get_db)
):
    db_task = db.query(models.Task).get(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    
    db.delete(db_task)
    db.commit()
