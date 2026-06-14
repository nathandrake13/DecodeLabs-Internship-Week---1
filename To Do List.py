tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter Task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added")

def view_task():
    if not tasks:
        print("Empty")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not completed"
        print(f"{index}. {task['task']} [{status}]")

def task_done():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):        
            tasks[index]["done"] = True
            print("Marked as Done")
        else:
            print("Invalid number")
    except ValueError:
        print("Enter a valid number")

def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):        
            removed = tasks.pop(index)
            print(f"Deleted Task: {removed['task']}")
        else:
            print("Invalid number")
    except ValueError:
        print("Enter a valid number")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        task_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Thank You")
        break
    else:
        print("Invalid choice. Try Again")