from controllers import TaskManagerController
from datetime import datetime

class CommandLineUI:
    def __init__(self):
        self.controller = None

    def _print_menu(self):
        print("To-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Edit the task")
        print("6. View overdue tasks")
        print("7. Load tasks from DAO")
        print("8. Save tasks to DAO")
        print("9. Quit")

    def run(self):
        name = input("Enter your name for the task list: ")
        email = input("Enter your email: ")
        self.controller = TaskManagerController(name, email)
        while True:
            self._print_menu()
            choice = input("Enter your choice: ")
            
            if choice == "1":
                task_type = input("Task type? (standard/recurring/priority): ").strip().lower()
                title = input("Enter a task: ")
                input_date = input("Enter a due date (YYYY-MM-DD): ")
                date_object = datetime.strptime(input_date, "%Y-%m-%d")
                if task_type == "recurring":
                    interval_days = int(input("Enter the recurrence interval in days: "))
                    self.controller.add_task(title, date_object, recurring=True, interval_days=interval_days)
                elif task_type == "priority":
                    while True:
                            try:
                                priority = int(input("Enter priority (1=low, 2=medium, 3=high): "))
                                if priority in [1, 2, 3]:
                                    break
                                else:
                                    print("Priority must be 1, 2, or 3.")
                            except ValueError:
                                print("Please enter a valid integer.")
                    description = input("Enter a description (optional): ")
                    self.controller.add_priority_task(title, priority, date_object, description)
                else:
                    self.controller.add_task(title, date_object)
            elif choice == "2":
                tasks = self.controller.get_tasks()
                for i, task in enumerate(tasks):
                    print(f"{i}: {task.title} (Due: {task.date_due}) Completed: {task.completed}")
            elif choice == "3":
                self.controller.get_tasks()
                try:
                    
                    ix = int(input("Enter the index of the task to remove: "))
                    self.controller.remove_task(ix)
                except Exception:
                    print("Invalid index. Please try again.")
            elif choice == "4":
                self.controller.get_tasks()
                try:
                    ix = int(input("Enter the index of the task to mark as completed: "))
                    if self.controller.mark_task_completed(ix):
                        print("Task marked as completed.")
                    else:
                        print("Invalid index.")
                except Exception:
                    print("Invalid index. Please try again.")
            elif choice == "5":
                self.controller.get_tasks()
                try:
                    ix = int(input("Enter the index of the task to edit: "))
                    print("1. Change title")
                    print("2. Change due date")
                    print("3. Change description")
                    edit_choice = input("Enter your choice: ")
                    if edit_choice == "1":
                        new_title = input("Enter the new title: ")
                        self.controller.edit_task(ix, title=new_title)
                    elif edit_choice == "2":
                        new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
                        date_object = datetime.strptime(new_due_date, "%Y-%m-%d")
                        self.controller.edit_task(ix, date_due=date_object)
                    elif edit_choice == "3":
                        new_description = input("Enter the new description: ")
                        self.controller.edit_task(ix, description=new_description)
                    else:
                        print("Invalid edit option.")
                except Exception:
                    print("Invalid index. Please try again.")
            elif choice == "6":
                overdue_tasks = self.controller.get_overdue_tasks()
                print("Overdue tasks:")
                for task in overdue_tasks:
                    print(f"{task.title} (Due: {task.date_due})")
            elif choice == "7":
                file_path = input("Enter the file path to load tasks from: ")
                self.controller.load_tasks(file_path)
                print("Tasks loaded from DAO.")
            elif choice == "8":
                file_path = input("Enter the file path to save tasks to: ")
                self.controller.save_tasks(file_path)
                print("Tasks saved to DAO.")
            elif choice == "9":
                break