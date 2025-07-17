from tasks import Task
from datetime import datetime
from users import Owner

class TaskList:
    """Represents a list of tasks for a specific user."""
    def __init__(self, owner: Owner) -> None:
        self.owner: Owner = owner
        self.tasks = []

    def add_task(self, task: Task) -> None:
        """Adds a task to the task list.
        Args:
            task (Task): The task to be added.
        """
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        """Removes a task from the task list by index.
        Args:
            ix (int): The index of the task to be removed.
        """   
        try:
            del self.tasks[ix]
            print(f"Task at index {ix} removed successfully.")
        except IndexError:
            print(f"No task found at index {ix}. Please enter a valid index.")

    def view_tasks(self) -> None: 
        """Displays uncompleted tasks in the task list with their indices. """
        print("The following tasks are still to be done:")
        for task in self.tasks:
            ix = self.tasks.index(task)
            print(f"{ix}: {task}")

    def view_overdue_tasks(self) -> None: 
        """Displays all overdue tasks in the task list."""
        for ix, task in enumerate(self.tasks):
            if task.date_due and task.date_due < datetime.now():
                print(ix, task)

    def get_task(self, ix: int) -> Task:
        """Returns a task from the task list by index.
        Args:
            ix (int): The index of the task to be retrieved.
        Returns:
            Task: The task at the specified index.
        """
        try:
            return self.tasks[ix]
        except IndexError:
            print(f"No task found at index {ix}. Please enter a valid index.")
            return None
        
    @property
    def uncompleted_tasks(self) -> list[Task]:
        """Returns a list of tasks that are not completed."""
        return [task for task in self.tasks if not task.completed]    