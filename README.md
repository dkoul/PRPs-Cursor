Cursor adaptation of Rasmus's work at https://github.com/Wirasm/PRPs-agentic-eng Please, buy him a coffee: https://coff.ee/wirasm

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

## Getting Started

### Option 1: Copy Resources to Your Existing Project

1. **Copy the Cursor workflows** to your project:

   ```bash
   # From your project root
   cp -r /path/to/PRPs-agentic-eng/cursor_workflows .
   cp /path/to/PRPs-agentic-eng/.cursorrules .
   ```

2. **Copy the PRP templates and runner**:

   ```bash
   cp -r /path/to/PRPs-agentic-eng/PRPs/templates PRPs/
   cp -r /path/to/PRPs-agentic-eng/PRPs/scripts PRPs/
   cp /path/to/PRPs-agentic-eng/PRPs/README.md PRPs/
   mkdir -p PRPs/completed
   ```

3. **Copy AI documentation** (optional but recommended):
   ```bash
   cp -r /path/to/PRPs-agentic-eng/PRPs/ai_docs PRPs/
   ```

### Option 2: Clone and Start a New Project

1. **Clone this repository**:

   ```bash
   git clone https://github.com/Wirasm/PRPs-agentic-eng.git
   cd PRPs-agentic-eng
   ```

2. **Create your project structure**:

   ```bash
   # Example for a Python project
   mkdir -p src/tests
   touch src/__init__.py
   touch pyproject.toml
   touch CURSOR.md
   ```

3. **Initialize with UV** (for Python projects):
   ```bash
   uv venv
   uv sync
   ```

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

## All Needed Context

### Documentation & References

- url: https://jwt.io/introduction/
  why: JWT structure and best practices

- file: src/auth/basic_auth.py
  why: Current auth pattern to replace

- doc: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
  section: OAuth2 with Password and JWT

### Known Gotchas

# CRITICAL: Use RS256 algorithm for production

# CRITICAL: Store refresh tokens in httpOnly cookies

# CRITICAL: Implement token blacklist for logout

## Implementation Blueprint

[... detailed implementation plan ...]

## Validation Loop

### Level 1: Syntax & Style

ruff check src/ --fix
mypy src/

### Level 2: Unit Tests

uv run pytest tests/test_auth.py -v

### Level 3: Integration Test

curl -X POST http://localhost:8000/auth/login \
 -H "Content-Type: application/json" \
 -d '{"email": "test@example.com", "password": "testpass"}'
```

## Project Structure Recommendations

```
your-project/
├── .cursorrules           # Cursor-specific rules and guidelines
├── cursor_workflows/      # Cursor workflows for PRP methodology
│   ├── prp_create.md      # Create comprehensive PRPs
│   ├── prp_execute.md     # Execute PRPs against codebase
│   ├── prime_context.md   # Load project context
│   └── code_review.md     # Review code changes
├── PRPs/
│   ├── templates/         # PRP templates
│   ├── scripts/          # PRP runner
│   ├── ai_docs/          # Library documentation
│   ├── completed/        # Finished PRPs
│   └── *.md              # Active PRPs
├── CURSOR.md             # Project-specific guidelines for Cursor
├── src/                  # Your source code
└── tests/                # Your tests
```

## Setting Up CURSOR.md

Create a `CURSOR.md` file in your project root with:

1. **Core Principles**: KISS, YAGNI, etc.
2. **Code Structure**: File size limits, function length
3. **Architecture**: How your project is organized
4. **Testing**: Test patterns and requirements
5. **Style Conventions**: Language-specific guidelines
6. **Development Commands**: How to run tests, lint, etc.

See the example CURSOR.md in this repository for a comprehensive template.

## Advanced Usage

### Running Multiple Sessions

Use Git worktrees for parallel development:

```bash
git worktree add -b feature-auth ../project-auth
git worktree add -b feature-api ../project-api

# Run Cursor in each worktree
cd ../project-auth && cursor .
cd ../project-api && cursor .
```


### Custom Workflows

Create your own workflows in `cursor_workflows/`:

```markdown
# cursor_workflows/my-workflow.md

# My Custom Workflow

## Purpose
Do something specific to my project.

## Usage
`@my-workflow.md <arguments>`

## Steps
[Your workflow implementation]
```

## Resources Included

### Cursor Workflows (cursor_workflows/)

- `prp_create.md` - Create comprehensive PRPs with research
- `prp_execute.md` - Execute PRPs against codebase
- `prime_context.md` - Load project context
- `code_review.md` - Review code changes

### Documentation (PRPs/ai_docs/)

- `cc_overview.md` - Core documentation
- `cc_common_workflows.md` - Common patterns
- `cc_troubleshoot.md` - Troubleshooting guide
- `cc_best_practices.md` - Best practices

### Templates (PRPs/templates/)

- `prp_base.md` - Comprehensive PRP template with validation
- `prp_spec.md` - Specification template
- `prp_planning.md` - Planning template with diagrams

