from fastapi.testclient import TestClient
from ToDoPlanner import app, todo_list

client = TestClient(app)

def setup_function():
    for day in todo_list:
        todo_list[day].clear()

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_root(): 
    response = client.get("/") 
    assert response.status_code == 200 
    assert response.json() == {"message": "Сервис работает"}

def test_version(): 
    response = client.get("/version")
    assert response.status_code == 200
    data = response.json()
    assert data["version"] == "0.1.0"
    assert isinstance(data["python"], str)

def test_add_todo_day_not_exist(client):
    response = client.post("/todos/funday", json={"task": "Сдать проект"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Дня недели не существует"
