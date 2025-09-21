from tasks import get_todays_tasks, display_tasks, parse_tasks

def test_get_todays_task():
    result = get_todays_tasks()

    assert isinstance(result, list)
    assert len(result) > 0
    assert all(isinstance(item, str) for item in result)


def test_parse_tasks():
    pass

def test_display_tasks():
    pass