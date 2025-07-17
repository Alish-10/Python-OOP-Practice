class User:
    # Represents a user of the to-do app.
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        
    def __str__(self) -> str:
        return f"User: {self.name}, Email: {self.email}"

class Owner(User):
    # Represents the owner of a task list.
    def __init__(self, name: str, email: str):
        super().__init__(name, email)

    def __str__(self) -> str:
        return f"Owner: {self.name}, Email: {self.email}"