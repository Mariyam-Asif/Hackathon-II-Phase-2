# ADR-2: In-Memory Storage Implementation

**Status**: Accepted
**Date**: 2026-01-02

## Context

The application requires a storage mechanism that aligns with the requirement of in-memory only data (no file system or database persistence). We need to choose an appropriate data structure for storing todo tasks that supports the required operations efficiently while maintaining the single-session nature of the application.

## Decision

We will use a dictionary (hash map) data structure with integer keys to store TodoTask objects in memory:
- **Structure**: `Dict[int, TodoTask]` - dictionary keyed by task ID with TodoTask objects as values
- **ID Generation**: Sequential integer IDs starting from 1
- **Operations**: O(1) average time complexity for read, update, and delete operations

## Alternatives Considered

1. **List-based storage**: Store TodoTask objects in a list/array
   - Pros: Simple implementation, maintains insertion order
   - Cons: O(n) lookup time for ID-based operations, inefficient for large datasets

2. **Dictionary-based storage (chosen)**: Store TodoTask objects in a dictionary keyed by ID
   - Pros: O(1) average time complexity for read, update, delete operations; efficient ID-based lookups
   - Cons: Slight memory overhead for hash table structure

3. **Class-based store with separate lists**: Maintain separate lists for different attributes
   - Pros: Could optimize for specific access patterns
   - Cons: More complex implementation, potential consistency issues

## Consequences

**Positive:**
- Efficient O(1) lookups, updates, and deletions by ID
- Aligns with requirement for in-memory storage only
- Supports the sequential ID assignment strategy
- Enables fast validation of task IDs
- Maintains clean separation in the data layer

**Negative:**
- Slight memory overhead compared to simple list storage
- Hash table implementation complexity (mitigated by using built-in Python dict)

## References

- `specs/1-todo-app/plan.md` - Component Design section (InMemoryStore)
- `specs/1-todo-app/data-model.md` - In-Memory Store Structure
- `specs/1-todo-app/spec.md` - Functional Requirements (FR-001, FR-008)