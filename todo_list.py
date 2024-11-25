# todo_list.py

todo_list = []

def add_task(task):
    todo_list.append(task)

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

# Sample usage
add_task("Finish homework")
add_task("Buy groceries")
view_tasks()
remove_task("Buy groceries")
view_tasks()
