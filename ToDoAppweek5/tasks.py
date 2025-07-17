import datetime
from typing import Optional

class Task:
    """Represents a task in a to-do list."""

    def __init__(self, title: str, date_due: datetime.datetime, description: Optional[str] = None):
        """
        Initializes a new Task object.

        Args:
            title (str): Title of the task.
            date_due (datetime.datetime): Due date of the task.
            description (Optional[str]): Description of the task (optional).
        """
        self.title: str = title
        self.date_created: datetime.datetime = datetime.datetime.now()
        self.date_due: datetime.datetime = date_due
        self.completed: bool = False
        self.description: Optional[str] = description

    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.completed = True

    def change_title(self, new_title: str) -> None:
        """Changes the title of the task."""
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        """Changes the due date of the task."""
        self.date_due = date_due

    def change_description(self, new_description: str) -> None:
        """Changes the description of the task."""
        self.description = new_description

    def __str__(self) -> str:
        """Returns a string representation of the task."""
        desc = f" | Description: {self.description}" if self.description else ""
        status = "Completed" if self.completed else "Pending"
        return (f"Title: {self.title} | Status: {status} | "
                f"Created: {self.date_created.strftime('%Y-%m-%d')} | "
                f"Due: {self.date_due.strftime('%Y-%m-%d')}{desc}")
        
    # ...existing Task code...

class RecurringTask(Task):
    """
    Represents a recurring task that repeats at a specified interval.
    """
    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta, description: Optional[str] = None):
        super().__init__(title, date_due, description)
        self.interval: datetime.timedelta = interval
        self.completed_dates: List[datetime.datetime] = []

    def mark_completed(self) -> None:
        """Mark the recurring task as completed and update the due date."""
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()
        self.completed = False  # Recurring tasks are never fully 'completed'

    def _compute_next_due_date(self) -> datetime.datetime:
        """Compute the next due date based on the interval."""
        return self.date_due + self.interval

    def __str__(self) -> str:
        completed_str = ", ".join([dt.strftime("%Y-%m-%d") for dt in self.completed_dates]) or "None"
        interval_str = f"Every {self.interval.days} days" if self.interval.days else f"Every {self.interval.seconds // 3600} hours"
        return (f"Recurring Task: {self.title} | Due: {self.date_due.strftime('%Y-%m-%d')} | "
                f"Interval: {interval_str} | Completed Dates: {completed_str}")