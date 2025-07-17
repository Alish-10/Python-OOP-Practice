from task_list import TaskList
from users import Owner
from task_factory import TaskFactory
from dao import TaskCsvDAO
from datetime import timedelta

class TaskManagerController:
    def __init__(self, owner_name, owner_email):
        self.owner = Owner(owner_name, owner_email)
        self.task_list = TaskList(self.owner)

    def add_task(self, title, date_due, recurring=False, interval_days=None):
        if recurring:
            task = TaskFactory.create_recurring_task(title, date_due, timedelta(days=interval_days))
        else:
            task = TaskFactory.create_task(title, date_due)
        self.task_list.add_task(task)
    def add_priority_task(self, title, priority, date_due, description=None):
        task = TaskFactory.create_priority_task(title, priority, date_due, description)
        self.task_list.add_task(task)

    def get_tasks(self):
        return self.task_list.tasks

    def remove_task(self, index):
        self.task_list.remove_task(index)

    def mark_task_completed(self, index):
        task = self.task_list.get_task(index)
        if task:
            task.mark_completed()
            return True
        return False

    def edit_task(self, index, title=None, date_due=None, description=None):
        task = self.task_list.get_task(index)
        if task:
            if title:
                task.change_title(title)
            if date_due:
                task.change_date_due(date_due)
            if description:
                task.change_description(description)
            return True
        return False

    def get_overdue_tasks(self):
        return self.task_list.get_overdue_tasks()

    def load_tasks(self, file_path):
        dao = TaskCsvDAO(file_path)
        loaded_tasks = dao.get_all_tasks()
        for task in loaded_tasks:
            self.task_list.add_task(task)

    def save_tasks(self, file_path):
        dao = TaskCsvDAO(file_path)
        dao.save_all_tasks(self.task_list.tasks)