import pytest
from consts import *


# Test isolation
@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


# Deploy contract for repeated tests without having to redeploy each time
@pytest.fixture(scope="module")
def todo(a, ToDo):
    return a[0].deploy(ToDo)


# Create a new task for repeated tests without having to recreate each time
@pytest.fixture(scope="module")
def createTask(a, todo):
    return todo.createTask(TASK_CREATED_DESC, { "from": a[0] })