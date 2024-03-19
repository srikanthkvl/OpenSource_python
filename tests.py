import reminder as app
from reminder import Task
import datetime as dt
import pytest


@pytest.fixture
def task_list():
    return [Task(name="Pay Rent"), Task(name="Buy Bread")]


@pytest.mark.parametrize(
    "date_input, expected_date", [("2024-04-01", dt.date(2024, 4, 1))]
)
def test_to_date(date_input, expected_date):
    assert app._to_date(date_input) == expected_date


@pytest.mark.parametrize(
    "date_input, expected_error_message",
    [
        ("2024-24-01", "2024-24-01 is not in YYYY-MM-DD format."),
        ("12345", "12345 is not in YYYY-MM-DD format."),
    ],
)
def test_to_date_exception(date_input, expected_error_message):
    with pytest.raises(ValueError, match=expected_error_message):
        app._to_date(date_input)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("Buy Bread", Task(name="Buy Bread")),
        ("Buy Banana", None),
        ("PAY RENT", Task(name="Pay Rent")),
    ],
)
def test_find_task(test_input, expected, task_list):
    assert app._find_task(test_input, task_list) == expected


def test_save_get_task_list(task_list):
    app._save_task_list(task_list)
    list = app._get_task_list()
    assert task_list == list


# def test_find_task_None():
#     task_list = [Task(name="Pay Rent"), Task(name="Buy Bread")]
#     assert app._find_task("Buy Banana", task_list) is None
