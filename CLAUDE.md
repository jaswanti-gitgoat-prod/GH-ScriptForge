# CLAUDE.md

This file provides guidance to Claude when working in this repository.

## Project Overview

This repository contains backend services and APIs.

Primary responsibilities:
- Implement backend features
- Debug production and development issues
- Write and maintain automated tests
- Improve reliability and performance
- Review existing code before making changes

---

# Development Principles

## Understand Before Changing

Before modifying code:

1. Read the surrounding implementation.
2. Understand why the code exists.
3. Look for existing patterns in the repository.
4. Reuse existing utilities whenever possible.
5. Avoid introducing duplicate logic.

Do not rewrite working code unless there is a clear benefit.

---

# Coding Guidelines

- Prefer readability over cleverness.
- Keep functions focused on a single responsibility.
- Use descriptive variable and function names.
- Minimize nesting.
- Remove dead code when appropriate.
- Keep changes as small as possible.

---

# Debugging Workflow

When investigating bugs:

1. Reproduce the issue.
2. Identify the root cause.
3. Explain why the bug occurs.
4. Propose the smallest safe fix.
5. Verify no regressions are introduced.

Do not guess at fixes without tracing the execution path.

---

# Testing

Testing is required for behavior changes.

When adding or modifying functionality:

- Update existing tests when appropriate.
- Add unit tests for business logic.
- Add integration tests for API behavior.
- Test happy paths and failure cases.
- Consider edge cases and invalid inputs.

Before considering work complete:

- All tests should pass.
- No new warnings should be introduced.
- Existing functionality should continue to work.

---

# API Guidelines

When modifying APIs:

- Preserve backward compatibility whenever possible.
- Validate all inputs.
- Return consistent error responses.
- Handle null and missing values safely.
- Document any breaking changes.

---

# Performance

Prefer:

- Efficient database queries
- Minimal network calls
- Avoiding unnecessary allocations
- Streaming large responses when appropriate

Do not optimize prematurely unless performance is a requirement.

---

# Error Handling

- Return actionable error messages.
- Log useful debugging information.
- Avoid exposing sensitive internal details.
- Fail predictably.

---

# Security

Always consider:

- Authentication
- Authorization
- Input validation
- SQL injection
- Command injection
- XSS where applicable
- Secret management

Never hardcode credentials or secrets.

---

# Logging

Logs should help diagnose issues without exposing sensitive information.

Include:

- Request identifiers
- Relevant IDs
- Error context
- Timing when useful

Do not log passwords, tokens, or secrets.

---

# Pull Request Expectations

Before submitting changes:

- Code builds successfully.
- Tests pass.
- Changes are minimal and focused.
- New functionality is covered by tests.
- Breaking changes are documented.

---

# Preferred Workflow

1. Understand the problem.
2. Inspect existing implementation.
3. Create a plan.
4. Implement minimal changes.
5. Add or update tests.
6. Run validation.
7. Summarize what changed and why.

---

# When Unsure

If requirements are ambiguous:

- Ask clarifying questions instead of making assumptions.
- Explain trade-offs.
- Recommend the safest implementation.

Accuracy is preferred over speed.
