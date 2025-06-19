from task_list import TaskList
from tasks import Task
import datetime

def propagate_task_list(task_list: TaskList) -> TaskList:
    """Propagates a task list with some sample tasks."""
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4), "Milk, eggs, bread"))
    task_list.add_task(Task("Do laundry", datetime.datetime.now() + datetime.timedelta(days=2)))
    task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=1), "Vacuum and dust"))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))
    task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)))
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6)))
    return task_list

def main() -> None:
    """Main function to run the To-Do List Manager."""
    owner = input("Enter your name for the task list: ")
    task_list = TaskList(owner)
    task_list = propagate_task_list(task_list)

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Edit a task (title, due date, description)")
        print("5. Mark a task as completed")
        print("6. View overdue tasks")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter a task: ")
            input_date = input("Enter a due date (YYYY-MM-DD): ")
            description = input("Enter a description (optional): ")
            try:
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object, description if description else None)
                task_list.add_task(task)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            task_list.view_tasks()
            try:
                ix = int(input("Enter the index of the task to remove: "))
                task_list.remove_task(ix)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            task_list.view_tasks()
            try:
                ix = int(input("Enter the index of the task to edit: "))
                if 1 <= ix <= len(task_list.tasks):
                    task = task_list.tasks[ix - 1]
                    print("1. Change title")
                    print("2. Change due date")
                    print("3. Change description")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == "1":
                        new_title = input("Enter new title: ")
                        task.change_title(new_title)
                        print("Title updated.")
                    elif sub_choice == "2":
                        new_due = input("Enter new due date (YYYY-MM-DD): ")
                        try:
                            new_due_date = datetime.datetime.strptime(new_due, "%Y-%m-%d")
                            task.change_date_due(new_due_date)
                            print("Due date updated.")
                        except ValueError:
                            print("Invalid date format.")
                    elif sub_choice == "3":
                        new_desc = input("Enter new description: ")
                        task.change_description(new_desc)
                        print("Description updated.")
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            task_list.view_tasks()
            try:
                ix = int(input("Enter the index of the task to mark as completed: "))
                if 1 <= ix <= len(task_list.tasks):
                    task_list.tasks[ix - 1].mark_completed()
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":
            task_list.view_overdue_tasks()

        elif choice == "7":
            print(f"Goodbye,{task_list.owner}!, see you next time!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()