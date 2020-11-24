# Tests the initial state of a fresh ToDo contract


def test_init_state(a, todo):
    assert todo.owner() == a[0]
    assert todo.taskCount() == 0
    assert todo.tasks(0) == (0, "", 0)
