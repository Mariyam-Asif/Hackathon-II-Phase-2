"""
In-memory storage implementation for todo tasks.
"""
from typing import Dict, List, Optional
from ..models.todo import TodoTask


class InMemoryStore:
    """
    Manages in-memory storage of tasks using a dictionary keyed by task ID.
    """
    def __init__(self):
        self._tasks: Dict[int, TodoTask] = {}
        self._next_id: int = 1

    def get_all(self) -> List[TodoTask]:
        """
        Retrieve all tasks from storage.

        Returns:
            List[TodoTask]: All tasks in the store
        """
        return list(self._tasks.values())

    def add(self, task: TodoTask) -> TodoTask:
        """
        Add a new task to storage.

        Args:
            task (TodoTask): The task to add

        Returns:
            TodoTask: The added task with assigned ID
        """
        # If the task doesn't have an ID (0 or negative), assign the next available ID
        if task.id <= 0:
            new_id = self._next_id
            self._next_id += 1
            # Create a new task with the assigned ID to avoid validation issues
            task_with_id = TodoTask(id=new_id, title=task.title, completed=task.completed)
            self._tasks[new_id] = task_with_id
            return task_with_id
        else:
            # If task already has a valid ID, use it
            self._tasks[task.id] = task
            return task

    def get_by_id(self, task_id: int) -> Optional[TodoTask]:
        """
        Retrieve a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[TodoTask]: The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def update(self, task_id: int, task: TodoTask) -> Optional[TodoTask]:
        """
        Update an existing task.

        Args:
            task_id (int): The ID of the task to update
            task (TodoTask): The updated task object

        Returns:
            Optional[TodoTask]: The updated task if successful, None if task doesn't exist
        """
        if task_id not in self._tasks:
            return None

        # Preserve the original ID
        task.id = task_id
        self._tasks[task_id] = task
        return task

    def delete(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if it didn't exist
        """
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True

    def exists(self, task_id: int) -> bool:
        """
        Check if a task exists by its ID.

        Args:
            task_id (int): The ID of the task to check

        Returns:
            bool: True if the task exists, False otherwise
        """
        return task_id in self._tasks

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            int: The next available ID
        """
        return self._next_id