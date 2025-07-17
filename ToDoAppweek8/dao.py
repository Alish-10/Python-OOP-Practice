from datetime import timedelta, datetime
from tasks import Task, RecurringTask, PriorityTask
from users import Owner
import csv

class TaskTestDAO:
    """Data Access Object for testing Task-related operations."""

    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

    def get_all_tasks(self) -> list[Task]:
        task_list = [
            Task("Buy groceries", datetime.now() - timedelta(days=4)),
            Task("Do laundry", datetime.now() - timedelta(days=-2)),
            Task("Clean room", datetime.now() + timedelta(days=-1)),
            Task("Do homework", datetime.now() + timedelta(days=3)),
            Task("Walk dog", datetime.now() + timedelta(days=5)),
            Task("Do dishes", datetime.now() + timedelta(days=6)),
            PriorityTask("Finish project", 3, date_due=datetime.now() + timedelta(days=2)),
        ]

        # sample recurring task
        r_task = RecurringTask("Go to the gym", datetime.now(), timedelta(days=7))
        r_task.completed_dates.append(datetime.now() - timedelta(days=7))
        r_task.completed_dates.append(datetime.now() - timedelta(days=14))
        r_task.completed_dates.append(datetime.now() - timedelta(days=22))
        r_task.date_created = datetime.now() - timedelta(days=28)
        task_list.append(r_task)
        return task_list

    def save_all_tasks(self, tasks: list[Task], owner: Owner = None) -> None:
        fieldnames = [
            "title", "type", "date_due", "completed", "interval", "completed_dates",
            "date_created", "priority", "description", "owner_name", "owner_email"
        ]
        with open(self.storage_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                row = {}
                row["title"] = task.title
                row["description"] = getattr(task, "description", "")
                # Owner info
                if owner:
                    row["owner_name"] = owner.name
                    row["owner_email"] = owner.email
                else:
                    row["owner_name"] = ""
                    row["owner_email"] = ""
                # Determine the type of task
                if isinstance(task, RecurringTask):
                    row["type"] = "RecurringTask"
                elif isinstance(task, PriorityTask):
                    row["type"] = "PriorityTask"
                else:
                    row["type"] = "Task"
                # Convert date_due to string format if it exists
                row["date_due"] = task.date_due.strftime("%Y-%m-%d") if task.date_due else ""
                # Store completed as "TRUE" or "FALSE"
                row["completed"] = "TRUE" if task.completed else "FALSE"
                # Handle interval and completed_dates for RecurringTask
                if isinstance(task, RecurringTask):
                    row["interval"] = str(task.interval) if task.interval else ""
                    row["completed_dates"] = ",".join(
                        d.strftime("%Y-%m-%d") for d in task.completed_dates
                    ) if task.completed_dates else ""
                else:
                    row["interval"] = ""
                    row["completed_dates"] = ""
                # Handle priority for PriorityTask
                if isinstance(task, PriorityTask):
                    row["priority"] = str(task.priority)
                else:
                    row["priority"] = ""
                # Format date_created
                row["date_created"] = task.date_created.strftime("%Y-%m-%d") if task.date_created else ""
                writer.writerow(row)

class TaskCsvDAO:
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path
        self.fieldnames = [
            "title", "type", "date_due", "completed", "interval", "completed_dates",
            "date_created", "priority", "description", "owner_name", "owner_email"
        ]
    
    def get_all_tasks(self) -> list[Task]:
        task_list = []
        with open(self.storage_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                task_type = row["type"]
                task_title = row["title"]
                task_date_due = datetime.strptime(row["date_due"], "%Y-%m-%d") if row["date_due"] else None
                task_completed = row["completed"] == "TRUE"
                task_date_created = datetime.strptime(row["date_created"], "%Y-%m-%d") if row["date_created"] else None
                description = row.get("description", None)
                priority = int(row["priority"]) if row.get("priority") and row["priority"].isdigit() else None

                if task_type == "RecurringTask":
                    interval_days = int(str(row["interval"]).split()[0]) if row["interval"] else 0
                    interval = timedelta(days=interval_days)
                    completed_dates = []
                    if row["completed_dates"]:
                        for date_str in row["completed_dates"].split(","):
                            if date_str.strip():
                                completed_dates.append(datetime.strptime(date_str.strip(), "%Y-%m-%d"))
                    task = RecurringTask(
                        task_title,
                        date_due=task_date_due,
                        interval=interval
                    )
                    task.completed = task_completed
                    task.date_created = task_date_created
                    task.completed_dates = completed_dates
                    task.description = description
                elif task_type == "PriorityTask":
                    task = PriorityTask(
                        task_title,
                        priority=priority,
                        completed=task_completed,
                        date_due=task_date_due,
                        description=description
                    )
                    task.date_created = task_date_created
                else:
                    task = Task(
                        task_title,
                        completed=task_completed,
                        date_due=task_date_due,
                        description=description
                    )
                    task.date_created = task_date_created
                task_list.append(task)
        return task_list
    
    def save_all_tasks(self, tasks: list[Task], owner: Owner = Owner) -> None:
        print("Saving tasks to CSV...")
        with open(self.storage_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for task in tasks:
                row = {}
                row["title"] = task.title
                row["description"] = getattr(task, "description", "")
                # Owner info
                if owner:
                    row["owner_name"] = owner.name
                    row["owner_email"] = owner.email
                else:
                    row["owner_name"] = ""
                    row["owner_email"] = ""
                # Determine the type of task
                if isinstance(task, RecurringTask):
                    row["type"] = "RecurringTask"
                elif isinstance(task, PriorityTask):
                    row["type"] = "PriorityTask"
                else:
                    row["type"] = "Task"
                # Convert date_due to string format if it exists
                row["date_due"] = task.date_due.strftime("%Y-%m-%d") if task.date_due else ""
                # Store completed as "TRUE" or "FALSE"
                row["completed"] = "TRUE" if task.completed else "FALSE"
                # Handle interval and completed_dates for RecurringTask
                if isinstance(task, RecurringTask):
                    row["interval"] = str(task.interval) if task.interval else ""
                    row["completed_dates"] = ",".join(
                        d.strftime("%Y-%m-%d") for d in task.completed_dates
                    ) if task.completed_dates else ""
                else:
                    row["interval"] = ""
                    row["completed_dates"] = ""
                # Handle priority for PriorityTask
                if isinstance(task, PriorityTask):
                    row["priority"] = str(task.priority)
                else:
                    row["priority"] = ""
                # Format date_created
                row["date_created"] = task.date_created.strftime("%Y-%m-%d") if task.date_created else ""
                writer.writerow(row)