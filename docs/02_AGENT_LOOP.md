# NADIA Agent Loop

Version: 0.1.0

Status: Draft

---

## Purpose

The Agent Loop is the core runtime of NADIA Agent.

Every autonomous task executed by NADIA Agent follows this loop.

---

## Execution Cycle

1. Receive Goal
2. Analyze Goal
3. Create Plan
4. Execute Step
5. Observe Result
6. Evaluate Outcome
7. Update Memory
8. Decide

---

## State Definitions

### Goal

A user request or scheduled task.

---

### Analyze

Understand the objective, constraints, available tools, and project context.

---

### Plan

Generate a sequence of executable steps.

The plan may be revised at any time.

---

### Execute

Run exactly one step.

Execution may use:

- Shell
- Python
- Git
- File System
- HTTP
- AI Provider

---

### Observe

Collect:

- command output
- errors
- generated files
- logs
- user feedback

---

### Evaluate

Determine whether:

- the step succeeded
- another attempt is needed
- the plan should change
- the task is finished

---

### Memory

Store useful information:

- decisions
- summaries
- fixes
- project knowledge

---

### Decide

Choose one action:

- Continue next step
- Retry
- Replan
- Ask user
- Finish task

---

## Design Rules

The Agent Loop must:

- execute one step at a time
- never skip observation
- never skip evaluation
- always update memory before finishing
- allow replanning when necessary

---

## Future Extensions

- Multi-Agent collaboration
- Parallel execution
- Long-running tasks
- Human approval checkpoints
- Background execution
