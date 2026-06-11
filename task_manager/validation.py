from datetime import datetime


def validate_non_empty_text(value, field_name):
    if value is None:
        raise ValueError(f"{field_name} cannot be empty.")
    value = value.strip()
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")
    return value


def validate_due_date(due_date):
    if due_date is None:
        raise ValueError("Due date must be a string.")
    due_date = due_date.strip()
    if due_date == "":
        return ""
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError:
        raise ValueError("Due date must use YYYY-MM-DD format.")
