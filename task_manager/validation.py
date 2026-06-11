from datetime import datetime

def validate_non_empty_text(value, field_name):
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    return value


def validate_due_date(due_date):
    if due_date is None:
        return None
    due_date = due_date.strip()
    if due_date == "":
        return ""
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError:
        return None
