# modified the structure of the given test code that was set considering flask app
# to match the django-drf api test
import requests
import json
import pytest

# URL of Django development server location
BASE_URL = 'http://localhost:8000/v1/tasks/'

def test_create_task():
    r = requests.post(BASE_URL, json={"title": "My First Task"})
    assert r.status_code == 201
    assert isinstance(r.json()["id"], int)
    assert len(r.json()) == 1

# def test_list_all_tasks():
#     r = requests.get(BASE_URL)
#     assert r.status_code == 200
#     assert isinstance(r.json()["tasks"], list)
#     assert len(r.json()["tasks"]) >= 1
#     assert isinstance(r.json()["tasks"][0]["id"], int)
#     assert isinstance(r.json()["tasks"][0]["title"], str)
#     assert isinstance(r.json()["tasks"][0]["is_completed"], bool)
#     assert len(r.json()["tasks"][0]) == 3

def test_list_all_tasks():
    r = requests.get(BASE_URL)
    assert r.status_code == 200
    assert isinstance(r.json(), list)  # Check if the response is a list
    assert len(r.json()) >= 1
    assert isinstance(r.json()[0]["id"], int)
    assert isinstance(r.json()[0]["title"], str)
    assert isinstance(r.json()[0]["is_completed"], bool)
    assert len(r.json()[0]) == 3

def test_get_task():
    r = requests.get(BASE_URL + '1/')
    assert r.status_code == 200
    assert isinstance(r.json(), dict)
    assert isinstance(r.json()["id"], int)
    assert isinstance(r.json()["title"], str)
    assert isinstance(r.json()["is_completed"], bool)
    assert len(r.json()) == 3

def test_update_task():
    r = requests.put(BASE_URL + '1/', json={"title": "My 1st Task", "is_completed": True})
    assert r.status_code == 204

def test_delete_task():
    r = requests.delete(BASE_URL + '1/')
    assert r.status_code == 204