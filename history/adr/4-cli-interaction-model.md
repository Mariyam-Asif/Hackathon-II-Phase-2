# ADR-4: CLI Interaction Model

**Status**: Accepted
**Date**: 2026-01-02

## Context

The application requires a command-line interface that provides efficient access to all core todo operations while maintaining good user experience. We need to choose between different interaction patterns that balance ease of use, efficiency, and discoverability for users familiar with command-line tools.

## Decision

We will implement a command-input loop interaction model:
- **Pattern**: Continuous command prompt where users enter commands directly
- **Format**: Simple commands like "add 'task'", "view", "update 1 'new task'", etc.
- **Flow**: Application runs continuously, accepting commands until "exit" is entered
- **User Experience**: Efficient for users familiar with CLI tools, minimal navigation

## Alternatives Considered

1. **Menu-driven interface**: Present numbered options for each operation
   - Pros: Highly discoverable, no need to remember command syntax
   - Cons: More navigation steps per operation, less efficient for frequent use

2. **Command-input loop (chosen)**: Continuous prompt accepting direct commands
   - Pros: Efficient for repeated operations, familiar to CLI users, faster operation
   - Cons: Requires users to remember command syntax, less discoverable initially

3. **Mixed approach**: Menu with option to enter commands directly
   - Pros: Best of both approaches
   - Cons: More complex implementation, inconsistent interaction model

## Consequences

**Positive:**
- Efficient interaction for users familiar with command-line tools
- Faster execution of repeated operations
- Clean, predictable command structure
- Aligns with typical CLI application patterns
- Supports scripting and automation potential

**Negative:**
- Steeper learning curve for users unfamiliar with CLI patterns
- Less discoverable than menu-driven interfaces
- Requires clear help documentation for command syntax
- Potential for user errors with command syntax

## References

- `specs/1-todo-app/plan.md` - API Contracts section (CLI Commands)
- `specs/1-todo-app/spec.md` - Functional Requirements (FR-007)
- `specs/1-todo-app/plan.md` - Decisions Documented section (CLI Flow Decision)