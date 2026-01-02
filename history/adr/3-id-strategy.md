# ADR-3: ID Strategy for Todo Tasks

**Status**: Accepted
**Date**: 2026-01-02

## Context

The application requires a unique identifier system for todo tasks that supports the core operations (add, view, update, delete, mark complete). The ID system must be intuitive for users when referencing tasks via the command-line interface while ensuring uniqueness within a session. The system should also support the progressive enhancement strategy for future phases.

## Decision

We will use sequential integer IDs starting from 1 for todo tasks:
- **Type**: Integer (int)
- **Generation**: Auto-incrementing starting from 1
- **Scope**: Unique within a single application session
- **User Experience**: Human-readable and easy to reference in CLI commands

## Alternatives Considered

1. **UUID/GUID strategy**: Use universally unique identifiers
   - Pros: Globally unique, no collision concerns, cryptographically secure
   - Cons: Not human-readable, difficult for users to reference in CLI, verbose output

2. **Sequential integer strategy (chosen)**: Auto-incrementing integers starting from 1
   - Pros: Human-readable, easy for users to reference, concise CLI commands, intuitive ordering
   - Cons: Not globally unique across sessions

3. **String-based identifiers**: User-defined or pattern-based IDs
   - Pros: Potentially meaningful to users
   - Cons: Complex validation, potential for duplicates, harder to ensure uniqueness

## Consequences

**Positive:**
- User-friendly IDs that are easy to reference in CLI commands
- Intuitive numbering system starting from 1
- Supports the CLI command format requirements (e.g., "update 1", "delete 2")
- Simple implementation and validation
- Aligns with user expectations for numbered lists

**Negative:**
- IDs are not globally unique across sessions
- Potential confusion if users expect persistence across sessions (mitigated by clear documentation)
- Requires maintaining a counter for ID generation

## References

- `specs/1-todo-app/plan.md` - Component Design section (TodoTask Model)
- `specs/1-todo-app/spec.md` - Functional Requirements (FR-011)
- `specs/1-todo-app/data-model.md` - TodoTask Entity fields