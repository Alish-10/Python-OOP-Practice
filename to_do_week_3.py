# Initialize an empty list to store tasks 
tasks = []

# Function to add a task to the list 
def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to view current tasks in the list 
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Current tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to remove a task from the list 
def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter the number of the task to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop 
while True:
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")