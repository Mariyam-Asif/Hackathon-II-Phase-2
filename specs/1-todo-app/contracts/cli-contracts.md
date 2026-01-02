# API Contracts: In-Memory Python Console-Based Todo Application

## CLI Operations Contract

### Operation: Add Todo
- **Command**: `add_todo(title: str)`
- **Input**: Task title/description (string, required)
- **Output**: TodoTask object with assigned ID
- **Success**: Returns created TodoTask with unique ID
- **Errors**:
  - ValidationError if title is empty or only whitespace

### Operation: List Todos
- **Command**: `list_todos()`
- **Input**: None
- **Output**: List of TodoTask objects
- **Success**: Returns all current TodoTask objects in the store
- **Errors**: None

### Operation: Update Todo
- **Command**: `update_todo(id: int, title: str)`
- **Input**: Task ID (integer, required), new title (string, required)
- **Output**: Updated TodoTask object
- **Success**: Returns updated TodoTask object
- **Errors**:
  - NotFoundError if task with given ID doesn't exist
  - ValidationError if new title is empty

### Operation: Delete Todo
- **Command**: `delete_todo(id: int)`
- **Input**: Task ID (integer, required)
- **Output**: Boolean indicating success
- **Success**: Returns True if task was deleted
- **Errors**:
  - NotFoundError if task with given ID doesn't exist

### Operation: Mark Complete
- **Command**: `mark_complete(id: int)`
- **Input**: Task ID (integer, required)
- **Output**: Updated TodoTask object
- **Success**: Returns TodoTask with completed status set to True
- **Errors**:
  - NotFoundError if task with given ID doesn't exist

## Data Contract: TodoTask
- **id**: Positive integer, unique within session
- **title**: String, non-empty, trimmed of whitespace
- **completed**: Boolean, default False