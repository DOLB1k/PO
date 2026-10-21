from datetime import date
import pytest

from library.circulation import Reader, CirculationError, issue_book


def test_issue_success():
    due = issue_book(Reader(id=1), True, date(2026, 1, 10))
    assert due == date(2026, 1, 24)


@pytest.mark.parametrize("reader,available,expected_error", [
    (Reader(id=2, active=False), True, "Reader is blocked"),
    (Reader(id=3, overdue=1), True, "Unresolved overdue loans"),
    (Reader(id=4), False, "No available instance"),
])
def test_issue_rejected(reader, available, expected_error):
    with pytest.raises(CirculationError, match=expected_error):
        issue_book(reader, available, date(2026, 1, 10))