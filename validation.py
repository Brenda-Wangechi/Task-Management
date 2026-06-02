from .validation import validate_non_empty_text, validate_due_date

tasks = []

def add_task():
    print("\nAdd Task")
    title = None
    while title is None:
        title_input = input("Task title: ")
        title = validate_non_empty_text(title_input, "Title")

    description = input("Task description (optional): ").strip()

    due_date = None
    while due_date is None:
        due_date_input = input("Due date (YYYY-MM-DD) or leave blank: ")
        due_date = validate_due_date(due_date_input)

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    print(f'Task "{title}" added successfully.')

def get_pending_tasks():
    return [task for task in tasks if not task["completed"]]

def mark_task_complete():
    pending = get_pending_tasks()
    if not pending:
        print("\nNo pending tasks to complete.")
        return

    print("\nPending Tasks:")
    for index, task in enumerate(pending, start=1):
        due = f' (due {task["due_date"]})' if task["due_date"] else ""
        print(f"{index}. {task['title']}{due}")

    selection = input("Enter the number of the task to mark complete: ").strip()
    if not selection.isdigit():
        print("Please enter a valid number.")
        return

    index = int(selection) - 1
    if index < 0 or index >= len(pending):
        print("Selection out of range.")
        return

    task_to_complete = pending[index]
    task_to_complete["completed"] = True
    print(f'Task "{task_to_complete["title"]}" marked complete.')

def view_pending_tasks():
    pending = get_pending_tasks()
    if not pending:
        print("\nNo pending tasks.")
        return

    print("\nPending Tasks:")
    for task in pending:
        due = f' | Due: {task["due_date"]}' if task["due_date"] else ""
        description = f' | {task["description"]}' if task["description"] else ""
        print(f'- {task["title"]}{description}{due}')

def view_progress():
    total = len(tasks)
    if total == 0:
        print("\nNo tasks added yet.")
        return

    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    percent = round((completed / total) * 100)
    print("\nProgress")
    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    print(f"Completion rate: {percent}%")
