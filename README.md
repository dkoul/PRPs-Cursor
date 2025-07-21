Cursor adaptation of Rasmus's work at https://github.com/Wirasm/PRPs-agentic-eng 
Please, buy him a coffee: https://coff.ee/wirasm

## What is PRP?

Product Requirement Prompt (PRP)

## In short

A PRP is PRD + curated codebase intelligence + agent/runbook—the minimum viable packet an AI needs to plausibly ship production-ready code on the first pass.

Product Requirement Prompt (PRP) is a structured prompt methodology first established in summer 2024 with context engineering at heart. A PRP supplies an AI coding agent with everything it needs to deliver a vertical slice of working software—no more, no less.

### How PRP Differs from Traditional PRD

A traditional PRD clarifies what the product must do and why customers need it, but deliberately avoids how it will be built.

A PRP keeps the goal and justification sections of a PRD yet adds three AI-critical layers:

### Context

Precise file paths and content, library versions and library context, code snippets examples. LLMs generate higher-quality code when given direct, in-prompt references instead of broad descriptions. Usage of a ai_docs/ directory to pipe in library and other docs.




## Using Cursor Workflows

The `cursor_workflows/` directory contains workflow files that integrate with Cursor's AI capabilities.

### Available Workflows

1. **PRP Creation & Execution**:
   - `@prime_context.md` - Load project context and understand PRP methodology
   - `@prp_create.md <feature>` - Generate comprehensive PRPs with research
   - `@prp_execute.md <prp-file>` - Execute PRPs against codebase

2. **Code Review**:
   - `@code_review.md` - Review code changes using PRP methodology

### How to Use Workflows

1. **In Cursor**, use the `@` symbol followed by the workflow name
2. **Example usage**:
   ```
   @prime_context.md
   @prp_create.md user authentication system with OAuth2
   @prp_execute.md PRPs/user-auth.md
   @code_review.md
   ```

## Using PRPs

### Creating a PRP

1. **Prime your context** first:
   ```
   @prime_context.md
   ```

2. **Create a comprehensive PRP**:
   ```
   @prp_create.md implement user authentication with JWT tokens
   ```

3. **Or manually use the template**:
   ```bash
   cp PRPs/templates/prp_base.md PRPs/my-feature.md
   ```

### Executing a PRP

1. **Using Cursor workflow** (recommended):
   ```
   @prp_execute.md PRPs/my-feature.md
   ```


### PRP Best Practices

1. **Context is King**: Include ALL necessary documentation, examples, and caveats
2. **Validation Loops**: Provide executable tests/lints the AI can run and fix
3. **Information Dense**: Use keywords and patterns from the codebase
4. **Progressive Success**: Start simple, validate, then enhance

### Example PRP Structure

```markdown
## Goal

Implement user authentication with JWT tokens

## Why

- Enable secure user sessions
- Support API authentication
- Replace basic auth with industry standard

## What

JWT-based authentication system with login, logout, and token refresh

### Success Criteria

- [ ] Users can login with email/password
- [ ] JWT tokens expire after 24 hours
- [ ] Refresh tokens work correctly
- [ ] All endpoints properly secured

