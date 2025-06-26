#python classes creation and initialization
#tasks: create a class for a to-do list manager, with methods to add, view, remove, mark as completed, and change the title of tasks.

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def change_title(self, new_title):
        self.title = new_title

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task: {self.title} [{status}]"

class TaskList:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added to {self.owner}'s task list.")

    def view_tasks(self):
        if not self.tasks:
            print(f"{self.owner}'s task list is empty.")
        else:
            print(f"{self.owner}'s tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task.title}' removed from {self.owner}'s task list.")
            
        else:
            print("Invalid task number.")

    def list_options(self):
        """Display the options for managing tasks."""
        while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark a task as completed")
            print("5. Change the title of a task")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter a task: ")
                task = Task(title)
                self.add_task(task)

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                if not self.tasks:
                    print("No tasks to remove.")
                else:
                    task_list_str = "\n".join([f"{idx}. {task.title}" for idx, task in enumerate(self.tasks, 1)])
                    ix = int(input(f"Enter the index of the task to remove:\n{task_list_str}\n> "))
                    self.remove_task(ix)

            elif choice == "4":
                if not self.tasks:
                    print("No tasks to mark as completed.")
                else:
                    task_list_str = "\n".join([f"{idx}. {task.title}" for idx, task in enumerate(self.tasks, 1)])
                    ix = int(input(f"Enter the index of the task to mark as completed:\n{task_list_str}\n> "))
                    if 0 < ix <= len(self.tasks):
                        self.tasks[ix - 1].mark_completed()
                        print(f"Task '{self.tasks[ix - 1].title}' marked as completed.")
                    else:
                        print("Invalid task number.")


            elif choice == "5":
                if not self.tasks:
                    print("No tasks to change title.")
                else:
                    task_list_str = "\n".join([f"{idx}. {task.title}" for idx, task in enumerate(self.tasks, 1)])
                    ix = int(input(f"Enter the index of the task to change title:\n{task_list_str}\n> "))
                    if 0 < ix <= len(self.tasks):
                        new_title = input("Enter the new title: ")
                        self.tasks[ix - 1].change_title(new_title)
                        print("Task title updated.")
                    else:
                        print("Invalid task number.")

            elif choice == "6":
                break

# Create instances OUTSIDE the class definition
my_task_list = TaskList("Alish")
print(f"Task list created for {my_task_list.owner}.")

# someone_elses_task_list = TaskList("John")
# print(f"Task list created for {someone_elses_task_list.owner}.")

# Test functionality
my_task_list.tasks = [Task("Do Homework"), Task("Do Laundry"), Task("Go Shopping")]
my_task_list.list_options()

