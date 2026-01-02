# Implementation Plan: In-Memory Python Console-Based Todo Application

**Branch**: `1-todo-app` | **Date**: 2026-01-02 | **Spec**: [specs/1-todo-app/spec.md](../specs/1-todo-app/spec.md)
**Input**: Feature specification from `/specs/1-todo-app/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a single-user, console-based todo application that stores all tasks in memory. The application provides core task management operations (add, view, update, delete, mark complete) through a command-line interface. The architecture follows a layered approach with clear separation between domain models, application logic, and interface components, designed to support future phases of the progressive todo application.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Standard Python library only (no external dependencies)
**Storage**: In-memory only, no persistence
**Testing**: [NEEDS CLARIFICATION] What level of testing is required for this phase?
**Target Platform**: Cross-platform console application (Windows, macOS, Linux)
**Project Type**: Single console application
**Performance Goals**: Sub-second response time for all operations
**Constraints**: No external services, APIs, or databases; console I/O only (stdin/stdout)
**Scale/Scope**: Single-user, single-session application

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Progressive Enhancement (Phase-Building)
- [x] Plan ensures each phase builds cleanly on the previous one without breaking abstractions
- [x] Each phase will be independently runnable while building toward the final system

### Simplicity First (Minimal Viable Solution)
- [x] Plan avoids premature optimization and over-engineering in early phases
- [x] Solutions will be minimal and readable before introducing complexity

### Separation of Concerns (Decoupled Architecture)
- [x] Plan maintains clear separation between business logic, data handling, UI, and infrastructure
- [x] API boundaries will have strong typing and validation

### Production Mindset (Best Practices)
- [x] Plan follows production-ready practices even in early phases
- [x] Security, observability, and testing standards will be maintained

### Extensibility (Future-Proof Design)
- [x] Plan anticipates future phases and maintains compatibility
- [x] Architectural decisions will support progressive enhancement strategy

### Independence and Scalability
- [x] Plan ensures each phase will be independently runnable
- [x] Dependencies will be properly scoped for each phase

## Project Structure

### Documentation (this feature)
```text
specs/1-todo-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
```text
src/
├── models/
│   └── todo.py          # TodoTask data model
├── services/
│   └── todo_service.py  # Business logic for todo operations
├── stores/
│   └── in_memory_store.py # In-memory storage implementation
└── cli/
    └── main.py          # Command-line interface and application entry point

pyproject.toml            # Project dependencies and metadata
README.md                # Project documentation
```

**Structure Decision**: Single project structure with clear separation of concerns. The application is organized into models (data structures), services (business logic), stores (data persistence layer), and cli (user interface). This structure supports the layered architecture with clear module boundaries that can be extended in future phases.

## Architecture Sketch

### Layered Application Design

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   CLI Layer     │    │  Service Layer  │    │   Data Layer    │
│                 │    │                 │    │                 │
│ - Command       │    │ - Task          │    │ - Task Model    │
│   parsing       │───▶│   operations    │───▶│ - In-memory     │
│ - Input/Output  │    │ - Validation    │    │   storage       │
│ - Error         │    │ - Business      │    │                 │
│   handling      │    │   logic         │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Component Design

#### 1. TodoTask Model
- **Purpose**: Defines the structure of a todo task
- **Attributes**:
  - id: int (auto-incrementing, unique identifier)
  - title: str (task description, non-empty)
  - completed: bool (completion status, default False)
- **Responsibilities**: Data representation and validation

#### 2. InMemoryStore
- **Purpose**: Manages in-memory storage of tasks
- **Attributes**:
  - tasks: Dict[int, TodoTask] (dictionary of tasks keyed by ID)
  - next_id: int (auto-incrementing ID counter)
- **Methods**:
  - get_all() -> List[TodoTask]
  - add(task: TodoTask) -> TodoTask
  - get_by_id(task_id: int) -> Optional[TodoTask]
  - update(task_id: int, task: TodoTask) -> Optional[TodoTask]
  - delete(task_id: int) -> bool
  - exists(task_id: int) -> bool
- **Responsibilities**: Data persistence (in memory), ID generation

#### 3. TodoService
- **Purpose**: Handles business logic for todo operations
- **Methods**:
  - add_task(title: str) -> TodoTask
  - get_all_tasks() -> List[TodoTask]
  - update_task(task_id: int, title: str) -> TodoTask
  - delete_task(task_id: int) -> bool
  - mark_completed(task_id: int) -> TodoTask
  - validate_task_id(task_id: int) -> bool
- **Responsibilities**: Task management, validation, business rules

#### 4. TodoCLI
- **Purpose**: Handles command-line interface and user interaction
- **Methods**:
  - run() -> None (main command loop)
  - parse_command(user_input: str) -> Command
  - handle_add(title: str) -> None
  - handle_view() -> None
  - handle_update(task_id: int, title: str) -> None
  - handle_delete(task_id: int) -> None
  - handle_complete(task_id: int) -> None
  - display_help() -> None
  - display_error(message: str) -> None
- **Responsibilities**: User interaction, command parsing, output formatting

### API Contracts

#### CLI Commands
```
add "task description"     # Add a new task
view                       # View all tasks
update 1 "new description" # Update task with ID 1
delete 1                   # Delete task with ID 1
complete 1                 # Mark task with ID 1 as completed
help                       # Show available commands
exit                       # Exit the application
```

#### Error Handling
- Invalid command: "Error: Unknown command. Type 'help' for available commands."
- Invalid task ID: "Error: Task with ID X does not exist."
- Empty description: "Error: Task description cannot be empty."
- General error: "Error: An unexpected error occurred."

## Implementation Approach

### Phase 1: Foundation (Research → Foundation)

1. **Research-Concurrent Development**
   - Research Python best practices for CLI applications while implementing
   - Follow APA citation style from Constitution for documentation
   - Organize work in Research → Foundation → Analysis → Synthesis phases

2. **Technical Implementation**
   - Create data models first (TodoTask)
   - Implement storage layer (InMemoryStore)
   - Build service layer (TodoService)
   - Develop CLI interface (TodoCLI)
   - Integrate all components

### Phase 2: Analysis & Synthesis

1. **Quality Validation**
   - Ensure clarity through comprehensive documentation
   - Verify modularity with clear separation of concerns
   - Validate spec compliance against acceptance criteria

2. **Testing Strategy**
   - Validate against acceptance criteria:
     - Add, View, Update, Delete, Mark Complete all work correctly
     - Data remains in-memory for session lifetime only
     - Deterministic and clear CLI output

## Decisions Documented

### In-Memory Storage Decision
- **Question**: List vs Dict for storage
- **Choice**: Dictionary (Dict[int, TodoTask]) for fast O(1) lookups
- **Rationale**: Better performance for ID-based operations vs sequential search in lists
- **Trade-off**: Slight memory overhead for significant performance gain

### ID Strategy Decision
- **Question**: Incremental vs UUID
- **Choice**: Sequential incremental integers starting from 1
- **Rationale**: Better readability for users vs UUIDs which are not user-friendly
- **Trade-off**: Global uniqueness vs user experience

### CLI Flow Decision
- **Question**: Menu loop vs command input
- **Choice**: Command input loop for better usability
- **Rationale**: More efficient for users familiar with CLI tools vs menu navigation
- **Trade-off**: Learning curve vs efficiency

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Layered architecture | Maintain separation of concerns | Single-file implementation would be harder to extend |
| Class-based storage | Better organization and testing | Global variables would create tight coupling |