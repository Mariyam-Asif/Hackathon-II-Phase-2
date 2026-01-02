# Quickstart: In-Memory Python Console-Based Todo Application

## Prerequisites
- Python 3.13 or higher
- UV package manager

## Setup
1. Clone or create the project directory
2. Navigate to the project root
3. Install dependencies: `uv sync` (or `pip install` if using standard pip)

## Running the Application
1. Navigate to the project root directory
2. Run: `python src/cli/main.py`
3. The application will display a menu with available options

## Basic Usage
1. **Add a task**: Select option 1, then enter your task description when prompted
2. **View all tasks**: Select option 2 to see all current tasks with their completion status
3. **Update a task**: Select option 3, enter the task ID and new description
4. **Delete a task**: Select option 4, enter the task ID to remove
5. **Mark task as completed**: Select option 5, enter the task ID

## Example Workflow
```
Welcome to the Todo Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Mark task as completed
6. Exit

Enter your choice: 1
Enter task description: Buy groceries
Task added successfully!

Enter your choice: 2
Tasks:
1. [ ] Buy groceries

Enter your choice: 5
Enter task ID to mark as completed: 1
Task marked as completed!

Enter your choice: 2
Tasks:
1. [x] Buy groceries

Enter your choice: 6
Goodbye!
```

## Error Handling
- Invalid task IDs will show an error message
- Empty task descriptions are not allowed
- The application will prompt for valid input if invalid data is entered