# Simple To-Do List Application
# Created to manage tasks in a clean and easy way

tasks = []

# Display menu
def show_menu():
    print("\n" + "="*30)
    print("      TO-DO LIST APP")
    print("="*30)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Exit")
    print("="*30)

# View tasks
def view_tasks():
    if not tasks:
        print("No tasks found! 😅")
    else:
        print("\nYour Tasks:")
        print("-"*30)
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task['completed'] else "✖"
            print(f"{i}. [{status}] {task['name']}")
        print("-"*30)

# Add task
def add_task():
    name = input("Enter task name: ")
    tasks.append({'name': name, 'completed': False})
    print(f"Task '{name}' added! ✅")

# Update task
def update_task():
    view_tasks()
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_name = input("Enter new task name: ")
            tasks[index]['name'] = new_name
            print("Task updated! ✏️")
        else:
            print("Invalid task number! ❌")
    except ValueError:
        print("Please enter a valid number! ❌")

# Delete task
def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed['name']}' deleted! 🗑️")
        else:
            print("Invalid task number! ❌")
    except ValueError:
        print("Please enter a valid number! ❌")

# Mark task complete
def mark_complete():
    view_tasks()
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            print(f"Task '{tasks[index]['name']}' marked complete! ✔️")
        else:
            print("Invalid task number! ❌")
    except ValueError:
        print("Please enter a valid number! ❌")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        mark_complete()
    elif choice == '6':
        print("Exiting To-Do List App. Goodbye! 👋")
        break
    else:
        print("Invalid choice! Try again 😅")
