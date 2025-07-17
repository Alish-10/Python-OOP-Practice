from datetime import datetime, timedelta
from tasks import Task, RecurringTask

class TaskFactory:
    @staticmethod
    def create_task(title: str, date_due: datetime, description: str = None) -> Task:
        return Task(title, completed=False, date_due=date_due, description=description)

    @staticmethod
    def create_recurring_task(title: str, date_due: datetime, interval: timedelta) -> RecurringTask:
        return RecurringTask(title, date_due=date_due, interval=interval)