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

def test_main_todo_workflow():
    post_response = client.post("/todos/friday", json={"task": "Сдать проект"})
    assert post_response.status_code == 200
    assert post_response.json()["added"] == "Сдать проект"
    get_response = client.get("/todos/friday")
    assert get_response.status_code == 200
    assert get_response.json()["tasks"] == ["Сдать проект"]

def test_invalid_day_error_handling():
    response = client.get("/todos/funday")
    assert response.status_code == 400
    assert response.json()["error"] == "Дня недели не существует"
