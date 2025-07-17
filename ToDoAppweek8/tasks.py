from datetime import datetime, timedelta

class Task:
    """Represents a task in the to-do list."""
    
    def __init__(
            self, 
            title: str, 
            completed: bool = False,
            date_due: datetime = None,
            description: str = None
    ) -> None:
        self.title: str = title
        self.completed: bool = completed
        self.date_created: datetime = datetime.now()
        self.date_due: datetime = date_due
        self.description: str = description

    def __str__(self) -> str:
        return f"Task: {self.title} | Completed: {self.completed} | Description: {self.description}"          
        
    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True
    
    def change_title(self, new_title: str) -> None:
        """Changes the title of the task.

        Args:
            new_title (str): The new title for the task.
        """
        self.title =  new_title

    def change_date_due(self, date_due: datetime) -> None:
        """Changes the due date of the task.
        Args:
            date_due (datetime): The new due date for the task.
        """
        self.date_due = date_due

    def change_description(self, description: str) -> None:
        """Changes the description of the task.
        
        Args:
            description (str): The new description for the task.
        """
        self.description = description   

class RecurringTask(Task):
    """Represents a recurring task in a to-do list.
    Args:
    Task (Task): The task to be repeated.
    """
    def __init__(self, title: str, date_due: datetime, interval: timedelta):
        """Creates a new recurring task.
        Args:
        title (str): Title of the task.
        date_due (datetime): Due date of the task.
        interval (timedelta): Interval between each repetition.
        """
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates : list[datetime] = [] # list of ddatetime objects
    
    def mark_completed(self) -> None:
        """Mark the recurring task as completed, update completed_dates and next due date."""
        self.completed_dates.append(datetime.now())
        self.date_due = self._compute_next_due_date()

    def _compute_next_due_date(self) -> datetime:
        """Computes the next due date of the task.
        Returns:
        datetime: The next due date of the task.
        """
        base_date = self.date_due if self.date_due is not None else datetime.now()
        return base_date + self.interval
    
    def __str__(self) -> str:        
        return f"{self.title} - Recurring (created: {self.date_created}, due: {self.date_due}, completed: {self.completed_dates}, interval: {self.interval})"
    # ...existing code...

class PriorityTask(Task):
    """Represents a task with a priority level (1=low, 2=medium, 3=high)."""
    PRIORITY_MAP: dict[int, str] = {1: 'low', 2: 'medium', 3: 'high'}

    def __init__(
        self,
        title: str,
        priority: int,
        completed: bool = False,
        date_due: datetime = None,
        description: str = None
    ) -> None:
        super().__init__(title, completed, date_due, description)
        if priority not in self.PRIORITY_MAP:
            raise ValueError("Priority must be 1 (low), 2 (medium), or 3 (high).")
        self.priority: int = priority

    def __str__(self) -> str:
        priority_str = self.PRIORITY_MAP[self.priority]
        return (f"PriorityTask: {self.title} | Priority: {priority_str} | "
                f"Completed: {self.completed} | Description: {self.description}")