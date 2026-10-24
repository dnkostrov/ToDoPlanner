import os
import logging
from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Список дел на неделю", version="0.1.0")

todo_list = {'monday': [], 'tuesday': [], 'wednesday': [], 'thursday': [], 'friday': [], 'saturday': [], 'sunday': []}

@app.get("/")
def root():
        return {"message": "Сервис работает"}

@app.get("/todos/{day}")
def get_todos(day: str):
    day = day.lower()
    if day not in todo_list:
        raise HTTPException(status_code=400, detail="Дня недели не существует")
    return {"day": day, "tasks": todo_list[day]}

@app.post("/todos/{day}")
def add_todo(day: str, task: str = Query(...)):
    day = day.lower()
    if day not in todo_list:
        raise HTTPException(status_code=400, detail="Дня недели не существует")
    if not task.strip():
        return {"error": "Текст задачи не может быть пустым"} 
    todo_list[day].append(task)
    return {"day": day, "added": task, "status": "ok"}

@app.delete("/todos/{day}/{task_id}")
def delete_todo(day: str, task_id: int):
    day = day.lower()
    if day not in todo_list:
        return {"error": "Дня недели не существует"}
    try:
        removed_task = todo_list[day].pop(task_id)
        return {"day": day, "removed": removed_task, "status": "ok"}
    except IndexError:
        return {"error": "Задачи с таким номером нет"}

@app.get("/version")
def get_version():
    return {"version": "0.1.0", "python": os.sys.version}

@app.get("/health")
def health():
    logger.info("Health check requested")
    return {"status": "ok"}

@app.get("/info")
def info():
    week_number = os.getenv("WEEK_NUMBER", "Номер недели не указан")
    app_user = os.getenv("APP_USER", "Пользователь не указан")

    return {
        "Номер недели": week_number,
        "Пользователь": app_user,
    }
