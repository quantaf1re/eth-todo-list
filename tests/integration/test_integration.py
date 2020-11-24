from consts import *


# Creates 2 tasks, progresses both, cancels one and
# completes the other - tests state after every action
# and the whole state of the contract at the end


def test_create_complete_and_cancel_tasks(a, todo):
    # Create 1st task
    d1 = "Description1"
    create1stTx = todo.createTask(d1, { "from": a[0] })

    task = todo.tasks(0)
    assert task[0] == 0
    assert task[1] == d1
    assert task[2] == STATUS[CREATED]
    assert todo.taskCount() == 1
    assert create1stTx.events["ModTask"][0]["id"] == 0
    assert create1stTx.events["ModTask"][0]["newStatus"] == STATUS[CREATED]

    # Create 2nd task
    d2 = "Description2"
    create2ndTx = todo.createTask(d2, { "from": a[0] })

    task = todo.tasks(1)
    assert task[0] == 1
    assert task[1] == d2
    assert task[2] == STATUS[CREATED]
    assert todo.taskCount() == 2
    assert create2ndTx.events["ModTask"][0]["id"] == 1
    assert create2ndTx.events["ModTask"][0]["newStatus"] == STATUS[CREATED]

    # Start working on 1st task
    modProgress1stTx = todo.modTask(0, STATUS[IN_PROGRESS], { "from": a[0]})

    assert todo.tasks(0)[2] == STATUS[IN_PROGRESS]
    assert modProgress1stTx.events["ModTask"][0]["id"] == 0
    assert modProgress1stTx.events["ModTask"][0]["newStatus"] == STATUS[IN_PROGRESS]

    # Get bored and start working on 2nd task
    modProgress2ndTx = todo.modTask(1, STATUS[IN_PROGRESS], { "from": a[0]})

    assert todo.tasks(1)[2] == STATUS[IN_PROGRESS]
    assert modProgress2ndTx.events["ModTask"][0]["id"] == 1
    assert modProgress2ndTx.events["ModTask"][0]["newStatus"] == STATUS[IN_PROGRESS]

    # Complete 2nd task
    modComplete2ndTx = todo.modTask(1, STATUS[COMPLETED], { "from": a[0]})

    assert todo.tasks(1)[2] == STATUS[COMPLETED]
    assert modComplete2ndTx.events["ModTask"][0]["id"] == 1
    assert modComplete2ndTx.events["ModTask"][0]["newStatus"] == STATUS[COMPLETED]

    # For some reason the 1st task becomes irrelevant
    modCancel1stTx = todo.modTask(0, STATUS[CANCELLED], { "from": a[0]})

    assert todo.tasks(0)[2] == STATUS[CANCELLED]
    assert modCancel1stTx.events["ModTask"][0]["id"] == 0
    assert modCancel1stTx.events["ModTask"][0]["newStatus"] == STATUS[CANCELLED]

    # General contract checks
    assert todo.owner() == a[0]
    assert todo.taskCount() == 2
    assert todo.tasks(2) == (0, "", 0)
    assert todo.tasks(0)[2] == STATUS[CANCELLED]
    assert todo.tasks(1)[2] == STATUS[COMPLETED]
