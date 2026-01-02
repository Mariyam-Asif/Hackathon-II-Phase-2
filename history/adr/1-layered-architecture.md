# ADR-1: Layered Architecture for Todo Application

**Status**: Accepted
**Date**: 2026-01-02

## Context

We need to structure the in-memory Python console-based todo application to ensure separation of concerns, maintainability, and extensibility for future phases. The application must support core task management operations (add, view, update, delete, mark complete) through a command-line interface while maintaining clean boundaries between different responsibilities.

## Decision

We will implement a three-layer architecture:
- **CLI Layer**: Handles command-line interface and user interaction
- **Service Layer**: Contains business logic for todo operations and validation
- **Data Layer**: Manages in-memory storage and data model definitions

## Alternatives Considered

1. **Monolithic approach**: Single file or class handling all responsibilities
   - Pros: Simpler for small applications
   - Cons: Difficult to maintain, test, and extend; violates separation of concerns

2. **MVC (Model-View-Controller)**: Traditional web application pattern
   - Pros: Well-known pattern
   - Cons: Overkill for CLI application; View responsibility overlaps with CLI layer

3. **Layered architecture (chosen)**: Clear separation between presentation, business logic, and data
   - Pros: Maintains separation of concerns, easy to test, extensible, aligns with constitution principles

## Consequences

**Positive:**
- Clear separation of concerns following constitution principle
- Easier to unit test individual components
- Supports progressive enhancement for future phases
- Maintains clean module boundaries
- Facilitates future API layer implementation

**Negative:**
- Slightly more complex initial setup
- More files and directories to navigate
- Potential over-engineering for very simple applications (mitigated by application scope)

## References

- `specs/1-todo-app/plan.md` - Architecture Sketch section
- `specs/1-todo-app/spec.md` - Requirements and constitution alignment