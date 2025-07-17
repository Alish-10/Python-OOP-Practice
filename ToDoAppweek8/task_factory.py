from datetime import datetime, timedelta
from tasks import Task, RecurringTask, PriorityTask

class TaskFactory:
    @staticmethod
    def create_task(title: str, date_due: datetime, description: str = None) -> Task:
        return Task(title, completed=False, date_due=date_due, description=description)

    @staticmethod
    def create_recurring_task(title: str, date_due: datetime, interval: timedelta) -> RecurringTask:
        return RecurringTask(title, date_due=date_due, interval=interval)
    @staticmethod
    def create_priority_task(title: str, priority: int, date_due: datetime, description: str = None) -> PriorityTask:
        """Creates a new priority task.
        
        Args:
            title (str): Title of the task.
            priority (int): Priority level of the task.
            date_due (datetime): Due date of the task.
            description (str, optional): Description of the task. Defaults to None.
        
        Returns:
            PriorityTask: A new priority task instance.
        """
        return PriorityTask(title, priority=priority, date_due=date_due, description=description)