from consts import *
from brownie import reverts


def test_modTask_in_progress(a, todoWithCreated):
    todoWithCreated.modTask(0, STATUS[IN_PROGRESS], { "from": a[0]})

    assert todoWithCreated.tasks(0)[2] == STATUS[IN_PROGRESS]


def test_modTask_completed(a, todoWithCreated):
    todoWithCreated.modTask(0, STATUS[COMPLETED], { "from": a[0]})

    assert todoWithCreated.tasks(0)[2] == STATUS[COMPLETED]


def test_modTask_cancelled(a, todoWithCreated):
    todoWithCreated.modTask(0, STATUS[CANCELLED], { "from": a[0]})

    assert todoWithCreated.tasks(0)[2] == STATUS[CANCELLED]


def test_createTask_revert_owner(a, todoWithCreated):
    with reverts(ONLY_OWNER_MSG):
        todoWithCreated.modTask(0, STATUS[IN_PROGRESS], { "from": a[1]})