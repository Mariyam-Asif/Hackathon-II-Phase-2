"""
Business logic service for todo operations.
"""
from typing import List, Optional
from ..models.todo import TodoTask
from ..stores.in_memory_store import InMemoryStore


class TodoService:
    """
    Handles business logic for todo operations including validation and task management.
    """
    def __init__(self, store: InMemoryStore):
        self._store = store

    def add_task(self, title: str) -> TodoTask:
        """
        Add a new task with the given title.

        Args:
            title (str): The title of the task

        Returns:
            TodoTask: The newly created task

        Raises:
            ValueError: If the title is empty or contains only whitespace
        """
        # Validate the task title
        validated_title = self._validate_task_title(title)

        # Create a new task with a placeholder ID (0) that will be replaced by the store
        task = TodoTask(id=-1, title=validated_title, completed=False)  # Using -1 as a clear placeholder
        return self._store.add(task)

    def get_all_tasks(self) -> List[TodoTask]:
        """
        Get all tasks from the store.

        Returns:
            List[TodoTask]: All tasks in the store
        """
        return self._store.get_all()

    def update_task(self, task_id: int, title: str) -> Optional[TodoTask]:
        """
        Update an existing task with a new title.

        Args:
            task_id (int): The ID of the task to update
            title (str): The new title for the task

        Returns:
            Optional[TodoTask]: The updated task if successful, None if task doesn't exist

        Raises:
            ValueError: If the title is empty or contains only whitespace
        """
        # Validate the task exists
        if not self.validate_task_id(task_id):
            return None

        # Validate the new title
        validated_title = self._validate_task_title(title)

        # Get the existing task and update its title
        existing_task = self._store.get_by_id(task_id)
        if existing_task is None:
            return None

        updated_task = TodoTask(id=task_id, title=validated_title, completed=existing_task.completed)
        return self._store.update(task_id, updated_task)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if it didn't exist
        """
        return self._store.delete(task_id)

    def mark_completed(self, task_id: int) -> Optional[TodoTask]:
        """
        Mark a task as completed.

        Args:
            task_id (int): The ID of the task to mark as completed

        Returns:
            Optional[TodoTask]: The updated task if successful, None if task doesn't exist
        """
        if not self.validate_task_id(task_id):
            return None

        existing_task = self._store.get_by_id(task_id)
        if existing_task is None:
            return None

        # Create an updated task with completed status
        completed_task = TodoTask(id=task_id, title=existing_task.title, completed=True)
        return self._store.update(task_id, completed_task)

    def validate_task_id(self, task_id: int) -> bool:
        """
        Validate if a task ID exists in the store.

        Args:
            task_id (int): The ID to validate

        Returns:
            bool: True if the task exists, False otherwise
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return False
        return self._store.exists(task_id)

    def _validate_task_title(self, title: str) -> str:
        """
        Validate and clean the task title.

        Args:
            title (str): The title to validate

        Returns:
            str: The validated and cleaned title

        Raises:
            ValueError: If the title is empty or contains only whitespace
        """
        if not isinstance(title, str):
            raise ValueError("Task title must be a string")

        cleaned_title = title.strip()
        if not cleaned_title:
            raise ValueError("Task title cannot be empty or contain only whitespace")

        return cleaned_title