from .tasks import add_task, mark_task_complete, view_pending_tasks, view_progress
from .validation import validate_non_empty_text, validate_due_date

__all__ = [
    "add_task",
    "mark_task_complete",
    "view_pending_tasks",
    "view_progress",
    "validate_non_empty_text",
    "validate_due_date",
]
from datetime import datetime

def validate_non_empty_text(value, field_name):
    value = value.strip()
    if not value:
        print(f"{field_name} cannot be empty.")
        return None
    return value

def validate_due_date(due_date):
    due_date = due_date.strip()
    if due_date == "":
        return ""
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError:
        print("Due date must use YYYY-MM-DD format.")
        return None