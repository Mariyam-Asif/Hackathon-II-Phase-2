"""
Command-line interface for the todo application.
"""
import sys
import os
from typing import Optional, List

# Add the project root to the Python path to allow imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.models.todo import TodoTask
from src.services.todo_service import TodoService
from src.stores.in_memory_store import InMemoryStore


class TodoCLI:
    """
    Handles command-line interface and user interaction for the todo application.
    """
    def __init__(self):
        self._store = InMemoryStore()
        self._service = TodoService(self._store)
        self._running = True

    def run(self) -> None:
        """
        Main command loop that runs the application.
        """
        print("Welcome to the Todo Application!")
        while self._running:
            self._display_menu()
            try:
                choice = input("Enter your choice: ").strip()
                self._handle_menu_choice(choice)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

    def _display_menu(self) -> None:
        """
        Display the main menu options.
        """
        print("\n1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as completed")
        print("6. Help")
        print("7. Exit")

    def _handle_menu_choice(self, choice: str) -> None:
        """
        Handle the user's menu choice.

        Args:
            choice (str): The user's menu choice
        """
        if choice == "1":
            self._handle_add()
        elif choice == "2":
            self._handle_view()
        elif choice == "3":
            self._handle_update()
        elif choice == "4":
            self._handle_delete()
        elif choice == "5":
            self._handle_complete()
        elif choice == "6":
            self._handle_help()
        elif choice == "7":
            self._handle_exit()
        else:
            self._display_error("Invalid choice. Please enter a number between 1 and 7.")

    def _handle_add(self) -> None:
        """
        Handle adding a new task.
        """
        try:
            title = input("Enter task description: ").strip()
            if not title:
                self._display_error("Task description cannot be empty.")
                return

            task = self._service.add_task(title)
            print(f"Task '{task.title}' added successfully with ID {task.id}!")
        except ValueError as e:
            self._display_error(str(e))
        except Exception as e:
            self._display_error(f"An unexpected error occurred: {str(e)}")

    def _handle_view(self) -> None:
        """
        Handle viewing all tasks.
        """
        try:
            tasks = self._service.get_all_tasks()
            if not tasks:
                print("No tasks found.")
                return

            print("Tasks:")
            for task in tasks:
                status = "[x]" if task.completed else "[ ]"
                print(f"{task.id}. {status} {task.title}")
        except Exception as e:
            self._display_error(f"An unexpected error occurred: {str(e)}")

    def _handle_update(self) -> None:
        """
        Handle updating an existing task.
        """
        try:
            task_id_str = input("Enter task ID to update: ").strip()
            if not task_id_str.isdigit():
                self._display_error("Task ID must be a number.")
                return

            task_id = int(task_id_str)
            if not self._service.validate_task_id(task_id):
                self._display_error(f"Task with ID {task_id} does not exist.")
                return

            new_title = input("Enter new task description: ").strip()
            if not new_title:
                self._display_error("Task description cannot be empty.")
                return

            updated_task = self._service.update_task(task_id, new_title)
            if updated_task:
                print(f"Task {task_id} updated successfully!")
            else:
                self._display_error(f"Failed to update task with ID {task_id}.")
        except ValueError as e:
            self._display_error(str(e))
        except Exception as e:
            self._display_error(f"An unexpected error occurred: {str(e)}")

    def _handle_delete(self) -> None:
        """
        Handle deleting a task.
        """
        try:
            task_id_str = input("Enter task ID to delete: ").strip()
            if not task_id_str.isdigit():
                self._display_error("Task ID must be a number.")
                return

            task_id = int(task_id_str)
            if not self._service.validate_task_id(task_id):
                self._display_error(f"Task with ID {task_id} does not exist.")
                return

            success = self._service.delete_task(task_id)
            if success:
                print(f"Task {task_id} deleted successfully!")
            else:
                self._display_error(f"Failed to delete task with ID {task_id}.")
        except ValueError as e:
            self._display_error(str(e))
        except Exception as e:
            self._display_error(f"An unexpected error occurred: {str(e)}")

    def _handle_complete(self) -> None:
        """
        Handle marking a task as completed.
        """
        try:
            task_id_str = input("Enter task ID to mark as completed: ").strip()
            if not task_id_str.isdigit():
                self._display_error("Task ID must be a number.")
                return

            task_id = int(task_id_str)
            if not self._service.validate_task_id(task_id):
                self._display_error(f"Task with ID {task_id} does not exist.")
                return

            completed_task = self._service.mark_completed(task_id)
            if completed_task:
                print(f"Task {task_id} marked as completed!")
            else:
                self._display_error(f"Failed to mark task {task_id} as completed.")
        except ValueError as e:
            self._display_error(str(e))
        except Exception as e:
            self._display_error(f"An unexpected error occurred: {str(e)}")

    def _handle_exit(self) -> None:
        """
        Handle exiting the application.
        """
        print("Goodbye!")
        self._running = False

    def _handle_help(self) -> None:
        """
        Handle displaying help information.
        """
        print("\nHelp - Todo Application Commands:")
        print("1. Add a new task - Enter a description for a new todo task")
        print("2. View all tasks - Display all current tasks with their completion status")
        print("3. Update a task - Modify the description of an existing task")
        print("4. Delete a task - Remove a task from the list")
        print("5. Mark task as completed - Change the status of a task to completed")
        print("6. Help - Show this help message")
        print("7. Exit - Quit the application")
        print("\nExamples:")
        print("- To add a task: Select option 1, then enter your task description")
        print("- To view tasks: Select option 2")
        print("- To update task ID 1: Select option 3, enter '1', then enter new description")
        print("- To delete task ID 1: Select option 4, enter '1'")
        print("- To mark task ID 1 as completed: Select option 5, enter '1'")

    def _display_error(self, message: str) -> None:
        """
        Display an error message.

        Args:
            message (str): The error message to display
        """
        print(f"Error: {message}")


def main():
    """
    Main entry point for the application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()