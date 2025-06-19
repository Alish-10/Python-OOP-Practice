from typing import List
from tasks import Task
import datetime

class TaskList:
    """Manages a list of Task objects for a specific owner."""

    def __init__(self, owner: str):
        """
        Initializes a new TaskList object.

        Args:
            owner (str): The name of the task list owner.
        """
        self.owner: str = owner
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Adds a task to the task list."""
        self.tasks.append(task)
        print(f"Task '{task.title}' added.")

    def remove_task(self, ix: int) -> None:
        """Removes a task by its index (1-based)."""
        if 1 <= ix <= len(self.tasks):
            removed = self.tasks.pop(ix - 1)
            print(f"Task '{removed.title}' removed.")
        else:
            print("Invalid task number.")

    def view_tasks(self) -> None:
        """Displays all tasks in the task list."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print(f"{self.owner}'s tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def view_overdue_tasks(self) -> None:
        """Displays all overdue tasks."""
        now = datetime.datetime.now()
        overdue = [task for task in self.tasks if not task.completed and task.date_due < now]
        if not overdue:
            print("No overdue tasks.")
        else:
            print("Overdue tasks:")
            for idx, task in enumerate(overdue, 1):
                print(f"{idx}. {task}")