# Python classes creation and initialization
# This script implements a to-do list manager with methods to add, view, remove, mark as completed, and change the title or due date of tasks.

import datetime

class Task:
    """Represents a single task in the to-do list."""
    def __init__(self, title, date_due):
        self.title = title
        # Date and time when the task was created
        self.date_created = datetime.datetime.now()
        self.date_due = date_due
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def change_title(self, new_title):
        self.title = new_title
        
    def change_date_due(self, new_date_due):
        self.date_due = new_date_due

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        due_date_str = self.date_due.strftime("%Y-%m-%d")
        return f"Task: {self.title} | Due: {due_date_str} | Status: {status}"

class TaskList:
    """Manages a list of Task objects for a specific owner."""
    def __init__(self, owner):
        # Owner's name (stored in uppercase)
        self.owner = owner.upper()
        # List of Task objects
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append(task)
        print(f"Task '{task.title}' added to {self.owner}'s task list.")

    def view_tasks(self):
        """Display all tasks in the list."""
        if not self.tasks:
            print(f"{self.owner}'s task list is empty.")
        else:
            print(f"{self.owner}'s tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def remove_task(self, task_number):
        """Remove a task by its index (1-based)."""
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task.title}' removed from {self.owner}'s task list.")
        else:
            print("Invalid task number.")

    def list_options(self):
        """Display the options for managing tasks and handle user input."""
        while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark a task as completed")
            print("5. Change the title of a task")
            print("6. Change the due date of a task")
            print("7. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Add a new task
                title = input("Enter a task: ")
                task_date_input = input("Enter a due date (YYYY-MM-DD): ")
                try:
                    date_object = datetime.datetime.strptime(task_date_input, "%Y-%m-%d")
                    task = Task(title, date_object)
                    self.add_task(task)
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")

            elif choice == "2":
                # View all tasks
                self.view_tasks()

            elif choice == "3":
                # Remove a task
                if not self.tasks:
                    print("No tasks to remove.")
                else:
                    task_list_str = "\n".join([f"{idx}. {task.title}" for idx, task in enumerate(self.tasks, 1)])
                    try:
                        ix = int(input(f"Enter the index of the task to remove:\n{task_list_str}\n> "))
                        self.remove_task(ix)
                    except ValueError:
                        print("Please enter a valid number.")

            elif choice == "4":
                # Mark a task as completed
                if not self.tasks:
                    print("No tasks to mark as completed.")
                else:
                    task_list_str = "\n".join([f"{idx}. {task.title}" for idx, task in enumerate(self.tasks, 1)])
                    try:
                        ix = int(input(f"Enter the index of the task to mark as completed:\n{task_list_str}\n> "))
                        if 0 < ix <= len(self.tasks):
                            self.tasks[ix - 1].mark_completed()
                            print(f"Task '{self.tasks[ix - 1].title}' marked as completed.")
                        else:
                            print("Invalid task number.")
                    except ValueError:
                        print("Please enter a valid number.")

            elif choice == "5":
                # Change the title of a task
                if not self.tasks:
                    print("No tasks to change title.")
                else:
                    task_list_str = "\n".join([f"{idx}. {task.title}" for idx, task in enumerate(self.tasks, 1)])
                    try:
                        ix = int(input(f"Enter the index of the task to change title:\n{task_list_str}\n> "))
                        if 0 < ix <= len(self.tasks):
                            new_title = input("Enter the new title: ")
                            self.tasks[ix - 1].change_title(new_title)
                            print("Task title updated.")
                        else:
                            print("Invalid task number.")
                    except ValueError:
                        print("Please enter a valid number.")
                        
            elif choice == "6":
                # Change the due date of a task
                if not self.tasks:
                    print("No tasks to change due date.")
                else:
                    task_list_str = "\n".join([f"{idx}. {task.title}" for idx, task in enumerate(self.tasks, 1)])
                    try:
                        ix = int(input(f"Enter the index of the task to change due date:\n{task_list_str}\n> "))
                        if 0 < ix <= len(self.tasks):
                            new_due_date_input = input("Enter the new due date (YYYY-MM-DD): ")
                            try:
                                new_due_date = datetime.datetime.strptime(new_due_date_input, "%Y-%m-%d")
                                self.tasks[ix - 1].change_date_due(new_due_date)
                                print(f"Task '{self.tasks[ix - 1].title}' due date updated.")
                            except ValueError:
                                print("Invalid date format. Please use YYYY-MM-DD.")
                        else:
                            print("Invalid task number.")
                    except ValueError:
                        print("Please enter a valid number.")

            elif choice == "7":
                # Quit the program
                print(f"Goodbye, {self.owner}!")
                break

            else:
                print("Invalid choice. Please try again.")

# Create an instance of TaskList for demonstration
my_task_list = TaskList("Alish")
print(f"Task list created for {my_task_list.owner}.")

# Add some sample tasks for testing
my_task_list.tasks = [
    Task("Buy groceries", datetime.datetime(2025, 5, 15)),
    Task("Complete Python assignment", datetime.datetime(2024, 5, 20)),
    Task("Book flight tickets", datetime.datetime(2025, 11, 1))
]

# Start the menu-driven interface
my_task_list.list_options()