# Prime Context Workflow

## Purpose
Prime Cursor with comprehensive project context to enable effective PRP creation and execution.

## Usage
`@prime_context.md`

## Context Loading Steps

### 1. Project Overview
**Load Core Information:**
- Read `README.md` for project purpose and structure
- Read `CLAUDE.md` for development guidelines
- Read `.cursorrules` for specific coding standards
- Understand the PRP methodology and framework

### 2. PRP Framework Understanding
**Core Concepts:**
- PRP = PRD + curated codebase intelligence + agent/runbook
- Goal: One-pass implementation success
- Context is King: Comprehensive documentation required
- Validation-First Design: Executable validation gates

**Key Principles:**
- Information dense prompts
- Progressive success approach
- Structured PRP format
- Validation loops for quality assurance

### 3. Project Structure
**Directory Layout:**
```
PRPs-agentic-eng/
├── cursor_workflows/     # Cursor-specific workflows
├── PRPs/
│   ├── templates/        # PRP templates
│   ├── scripts/         # PRP runner utilities
│   ├── ai_docs/         # Curated documentation
│   ├── completed/       # Finished PRPs
│   └── *.md             # Active PRPs
├── claude_md_files/     # Framework examples
└── pyproject.toml       # Python configuration
```

### 4. Available Templates
**PRP Templates:**
- `PRPs/templates/prp_base.md` - Comprehensive PRP template
- `PRPs/templates/prp_spec.md` - Specification template
- `PRPs/templates/prp_planning.md` - Planning template
- `PRPs/templates/prp_task.md` - Task template

### 5. Available Workflows
**Cursor Workflows:**
- `cursor_workflows/prp_create.md` - Create new PRPs
- `cursor_workflows/prp_execute.md` - Execute existing PRPs
- `cursor_workflows/prime_context.md` - Load project context
- `cursor_workflows/code_review.md` - Review code changes

### 6. Development Commands
**PRP Execution:**
```bash
# Interactive mode
uv run PRPs/scripts/prp_runner.py --prp [name] --interactive --model cursor

# Headless mode
uv run PRPs/scripts/prp_runner.py --prp [name] --output-format json --model cursor
```

**Validation Commands:**
```bash
# Syntax and style
ruff check --fix && mypy .

# Unit tests
uv run pytest tests/ -v
```

### 7. Best Practices
**PRP Creation:**
- Start with comprehensive research
- Include all necessary context
- Design executable validation gates
- Reference existing patterns
- Aim for 8+ confidence score

**PRP Execution:**
- Follow structured workflow
- Implement progressively
- Validate continuously
- Use subagents for parallel work
- Test thoroughly

### 8. Quality Standards
**Anti-Patterns to Avoid:**
- Minimal context prompts
- Skipping validation steps
- Ignoring structured format
- Creating new patterns unnecessarily
- Hardcoding configuration values

**Success Metrics:**
- One-pass implementation success
- All validation gates pass
- Code follows existing patterns
- No regressions introduced

## Context Primed
After running this workflow, you should understand:
- The PRP methodology and its purpose
- Available templates and workflows
- Project structure and conventions
- Development commands and validation
- Quality standards and best practices

You're now ready to effectively create and execute PRPs using Cursor!

## Next Steps
- Use `@prp_create.md` to create new PRPs
- Use `@prp_execute.md` to implement existing PRPs
- Use `@code_review.md` to review changes
- Always validate your work thoroughly

Remember: **The goal is one-pass implementation success through comprehensive context.** 