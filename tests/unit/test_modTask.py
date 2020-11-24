from consts import *
from brownie import reverts


# Should execute
def test_modTask_in_progress(a, todoWithCreated):
    todoWithCreated.modTask(0, STATUS[IN_PROGRESS], { "from": a[0]})

    assert todoWithCreated.tasks(0)[2] == STATUS[IN_PROGRESS]


def test_modTask_completed(a, todoWithCreated):
    todoWithCreated.modTask(0, STATUS[COMPLETED], { "from": a[0]})

    assert todoWithCreated.tasks(0)[2] == STATUS[COMPLETED]


def test_modTask_cancelled(a, todoWithCreated):
    todoWithCreated.modTask(0, STATUS[CANCELLED], { "from": a[0]})

    assert todoWithCreated.tasks(0)[2] == STATUS[CANCELLED]


# Should revert
def test_modTask_revert_owner(a, todoWithCreated):
    with reverts(ONLY_OWNER_MSG):
        todoWithCreated.modTask(0, STATUS[IN_PROGRESS], { "from": a[1]})


def test_modTask_revert_doesnt_exist(a, todoWithCreated):
    with reverts("Task doesn't exist"):
        todoWithCreated.modTask(1, STATUS[IN_PROGRESS], { "from": a[0]})


# Status only supports 0-3 inclusive
def test_modTask_revert_status_doesnt_exist(a, todoWithCreated):
    with reverts():
        todoWithCreated.modTask(0, 4, { "from": a[1]})