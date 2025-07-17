from users import Owner
from task_list import TaskList
from tasks import Task, RecurringTask
from dao import TaskTestDAO, TaskCsvDAO
from datetime import datetime, timedelta

def main() -> None:
    # Gather owner information and create the task list
    name = input("Enter your name for the task list: ")
    email = input("Enter your email: ")
    owner = Owner(name, email)
    task_list = TaskList(owner)
    # task_list = propagate_task_list(task_list)
    while True:
        # Display the menu options
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
            
        choice = input("Enter your choice: ") 
            
        if choice == "1":
            task_type = input("Do you want to add a recurring task? (y/n): ").strip().lower()
            title = input("Enter a task: ")
            input_date = input("Enter a due date (YYYY-MM-DD): ")
            date_object = datetime.strptime(input_date, "%Y-%m-%d")
            if task_type == "y":
                interval_days = int(input("Enter the recurrence interval in days: "))
                interval = timedelta(days=interval_days)
                task = RecurringTask(title, date_due=date_object, interval=interval)
                task_list.add_task(task)
            else:
                task = Task(title, completed=False, date_due=date_object)
                task_list.add_task(task)

        elif choice == "2":
            task_list.view_tasks()
            print("DEBUG:", len(task_list.tasks))

        elif choice == "3":
            ix = int(input("Enter the index of the task to remove: "))
            task_list.remove_task(ix)
            
        elif choice == "4":
            ix = int(input("Enter the index of the task to mark as completed: "))
            task = task_list.get_task(ix)
            if task:
                task.mark_completed()
                print(f"Task '{task.title}' marked as completed.")

        elif choice == "5":
            ix = int(input("Enter the index of the task to edit: "))
            task = task_list.get_task(ix)
            if task:
                print("1. Change title")
                print("2. Change due date")
                print("3. Change description")
                edit_choice = input("Enter your choice: ")
                if edit_choice == "1":
                    new_title = input("Enter the new title: ")
                    task.change_title(new_title)
                    print(f"Task title changed to '{new_title}'.")
                elif edit_choice == "2":
                    new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
                    date_object = datetime.strptime(new_due_date, "%Y-%m-%d")
                    task.change_date_due(date_object)
                    print(f"Task due date changed to '{new_due_date}'.")
                elif edit_choice == "3":
                    new_description = input("Enter the new description: ")
                    task.change_description(new_description)
                    print("Task description changed.")
                else:
                    print("Invalid edit option.")
            else:
                print("Invalid index.")
        elif choice == "6":
            print("Overdue tasks:")
            task_list.view_overdue_tasks()
        elif choice == "7":
            file_path = input("Enter the file path to load tasks from: ")
            dao = TaskCsvDAO(file_path)
            loaded_tasks = dao.get_all_tasks()
            for task in loaded_tasks:
                task_list.add_task(task)
            print("Tasks loaded from DAO.")
        elif choice == "8":
            file_path = input("Enter the file path to save tasks to: ")
            dao = TaskCsvDAO(file_path)
            dao.save_all_tasks(task_list.tasks)
            print("Tasks saved to DAO.")
        elif choice == "9":
            break


if __name__ == "__main__":
    main()

