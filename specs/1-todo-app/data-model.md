# Data Model: In-Memory Python Console-Based Todo Application

## TodoTask Entity

### Fields
- **id** (int): Unique identifier for the task, auto-incrementing integer
- **title** (str): Text description of the task, required field
- **completed** (bool): Boolean indicating completion status, default False

### Relationships
- No relationships with other entities (standalone entity)

### Validation Rules
- **id**: Must be a positive integer, auto-generated
- **title**: Must be non-empty string (1+ characters), trimmed of leading/trailing whitespace
- **completed**: Must be boolean value (True/False)

### State Transitions
- **Initial State**: `completed = False` when task is created
- **Completed State**: `completed = True` when task is marked as completed
- **Update State**: `title` can be modified while maintaining the same `id`

### Constraints
- Each `id` must be unique within the application session
- `title` cannot be empty or contain only whitespace
- Task state changes only through defined operations (no direct property modification)

## In-Memory Store Structure

### Storage Mechanism
- Dictionary keyed by `id` with `TodoTask` objects as values
- Separate counter for generating unique IDs

### Operations Supported
- **Create**: Add new TodoTask with unique ID
- **Read**: Retrieve TodoTask by ID
- **Update**: Modify existing TodoTask properties
- **Delete**: Remove TodoTask by ID
- **List**: Retrieve all TodoTask objects