from typing import List
from tasks import Task
from users import Owner
import datetime

class TaskList:
    """Manages a list of Task objects for a specific owner."""

    def __init__(self, owner: Owner):
        """
        Initializes a new TaskList object.

        Args:
            owner (Owner): The owner of the task list.
        """
        self.owner: Owner = owner
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
            print(f"{self.owner.name}'s tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def view_overdue_tasks(self) -> None:
        """Displays all overdue tasks."""
        now = datetime.datetime.now()
        overdue_tasks = [task for task in self.tasks if task.date_due < now and not task.completed]
        
        if not overdue_tasks:
            print("No overdue tasks.")
        else:
            print("Overdue tasks:")
            for idx, task in enumerate(overdue_tasks, 1):
                print(f"{idx}. {task}")