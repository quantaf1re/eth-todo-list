from consts import *


def test_create_complete_and_cancel_tasks(a, todo):
    # Create 1st task
    d1 = "Description1"
    todo.createTask(d1, { "from": a[0] })

    task = todo.tasks(0)
    assert task[0] == 0
    assert task[1] == d1
    assert task[2] == STATUS[CREATED]
    assert todo.taskCount() == 1

    # Create 2nd task
    d2 = "Description2"
    todo.createTask(d2, { "from": a[0] })

    task = todo.tasks(1)
    assert task[0] == 1
    assert task[1] == d2
    assert task[2] == STATUS[CREATED]
    assert todo.taskCount() == 2

    # Start working on 1st task
    todo.modTask(0, STATUS[IN_PROGRESS], { "from": a[0]})

    assert todo.tasks(0)[2] == STATUS[IN_PROGRESS]

    # Get bored and start working on 2nd task
    todo.modTask(1, STATUS[IN_PROGRESS], { "from": a[0]})

    assert todo.tasks(1)[2] == STATUS[IN_PROGRESS]

    # Complete 2nd task
    todo.modTask(1, STATUS[COMPLETED], { "from": a[0]})

    assert todo.tasks(1)[2] == STATUS[COMPLETED]

    # For some reason the 1st task becomes irrelevant
    todo.modTask(1, STATUS[CANCELLED], { "from": a[0]})

    assert todo.tasks(1)[2] == STATUS[CANCELLED]

    # General contract checks
    assert todo.owner() == a[0]
    assert todo.taskCount() == 2
    assert todo.tasks(2) == (0, "", 0)
