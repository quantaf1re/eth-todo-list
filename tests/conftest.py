import pytest
from consts import *


# test isolation, always use!
@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


# contract deployment
@pytest.fixture(scope="module")
def todo(a, ToDo):
    yield a[0].deploy(ToDo)


# contract deployment
@pytest.fixture(scope="module")
def todoWithCreated(a, todo):
    todo.createTask(TASK_CREATED_DESC, { "from": a[0] })
    yield todo