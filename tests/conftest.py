import pytest


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
def taskCreated(a, todo):
    todo.createTask("First task", { "from": a[0] })