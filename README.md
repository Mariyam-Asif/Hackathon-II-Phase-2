# In-Memory Python Console-Based Todo Application

A simple, single-user console application for managing todo tasks in memory. This application provides core task management operations through a command-line interface without any persistence.

## Features

- Add new todo tasks
- View all current tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- In-memory storage (tasks persist only for the session)

## Prerequisites

- Python 3.13 or higher

## Setup

1. Clone or download this repository
2. Navigate to the project directory
3. No additional installation required (uses only Python standard library)

## Running the Application

To run the application, execute:

```bash
python src/cli/main.py
```

## Usage

The application provides a menu-driven interface:

1. **Add a new task** - Enter a description for a new todo task
2. **View all tasks** - Display all current tasks with their completion status
3. **Update a task** - Modify the description of an existing task
4. **Delete a task** - Remove a task from the list
5. **Mark task as completed** - Change the status of a task to completed
6. **Exit** - Quit the application

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

## Architecture

The application follows a layered architecture:

- **Models**: Data structures (TodoTask)
- **Services**: Business logic (TodoService)
- **Stores**: Data persistence (InMemoryStore)
- **CLI**: User interface (TodoCLI)

## License

[Specify your license here]