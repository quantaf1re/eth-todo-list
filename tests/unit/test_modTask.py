from consts import *
from brownie import reverts


# Should execute
def test_modTask_in_progress(a, todo, createTask):
    tx = todo.modTask(0, STATUS[IN_PROGRESS], { "from": a[0]})

    assert todo.tasks(0)[2] == STATUS[IN_PROGRESS]
    assert tx.events["ModTask"][0]["id"] == 0
    assert tx.events["ModTask"][0]["newStatus"] == STATUS[IN_PROGRESS]


def test_modTask_completed(a, todo, createTask):
    tx = todo.modTask(0, STATUS[COMPLETED], { "from": a[0]})

    assert todo.tasks(0)[2] == STATUS[COMPLETED]
    assert tx.events["ModTask"][0]["id"] == 0
    assert tx.events["ModTask"][0]["newStatus"] == STATUS[COMPLETED]


def test_modTask_cancelled(a, todo, createTask):
    tx = todo.modTask(0, STATUS[CANCELLED], { "from": a[0]})

    assert todo.tasks(0)[2] == STATUS[CANCELLED]
    assert tx.events["ModTask"][0]["id"] == 0
    assert tx.events["ModTask"][0]["newStatus"] == STATUS[CANCELLED]


# Should revert
def test_modTask_revert_owner(a, todo, createTask):
    with reverts(ONLY_OWNER_MSG):
        todo.modTask(0, STATUS[IN_PROGRESS], { "from": a[1]})


def test_modTask_revert_doesnt_exist(a, todo, createTask):
    with reverts("Task doesn't exist"):
        todo.modTask(1, STATUS[IN_PROGRESS], { "from": a[0]})


# Status only supports 0-3 inclusive
def test_modTask_revert_status_doesnt_exist(a, todo, createTask):
    with reverts():
        todo.modTask(0, 4, { "from": a[1]})