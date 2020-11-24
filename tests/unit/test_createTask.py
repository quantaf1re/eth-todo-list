from consts import *
from brownie import reverts


# Should execute
def test_task_created(todoWithCreated):
    task = todoWithCreated.tasks(0)
    assert task[0] == 0
    assert task[1] == TASK_CREATED_DESC
    assert task[2] == STATUS[CREATED]
    assert todoWithCreated.taskCount() == 1


# Should revert
def test_createTask_revert_owner(a, todo):
    with reverts(ONLY_OWNER_MSG):
        todo.createTask("Junk description", { "from": a[1]})


def test_createTask_revert_description(a, todo):
    with reverts("Need a description!"):
        todo.createTask("", { "from": a[0]})