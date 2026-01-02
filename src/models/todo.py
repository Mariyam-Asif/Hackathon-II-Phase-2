"""
TodoTask data model for the in-memory todo application.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class TodoTask:
    """
    Represents a single todo task with id, title, and completion status.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Task description
        completed (bool): Completion status, default False
    """
    id: int
    title: str
    completed: bool = False

    def __post_init__(self):
        """Validate the TodoTask after initialization."""
        # Allow special ID of -1 during creation, which will be replaced by the store
        if not isinstance(self.id, int) or (self.id <= 0 and self.id != -1):
            if self.id != -1:  # Only raise error if not the special creation ID
                raise ValueError("ID must be a positive integer")

        if not isinstance(self.title, str):
            raise ValueError("Title must be a string")

        if not self.title.strip():
            raise ValueError("Title cannot be empty or contain only whitespace")

        if not isinstance(self.completed, bool):
            raise ValueError("Completed status must be a boolean")

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Title must be a string")

        if not value.strip():
            raise ValueError("Title cannot be empty or contain only whitespace")

        self._title = value.strip()