# Cursor Rules for PRP Framework

## Project Nature
This is a **PRP (Product Requirement Prompt) Framework** repository. The core concept: **"PRP = PRD + curated codebase intelligence + agent/runbook"** - designed to enable AI agents to ship production-ready code on the first pass.

## Core Principles
- **Context is King**: Include ALL necessary documentation, examples, and caveats in PRPs
- **Validation-First Design**: Every PRP must contain executable validation gates
- **One-Pass Implementation**: Design for success on first execution
- **Information Dense**: Use keywords and patterns from the codebase
- **Progressive Success**: Start simple, validate, then enhance

## PRP Structure Requirements

### Required Sections for Every PRP:
1. **Goal**: Specific end state and desires
2. **Why**: Business value and user impact  
3. **What**: User-visible behavior and technical requirements
4. **All Needed Context**: Documentation URLs, code examples, gotchas, patterns
5. **Implementation Blueprint**: Pseudocode with critical details and task lists
6. **Validation Loop**: Executable commands for syntax, tests, integration

### PRP Validation Gates (Must be Executable)
```bash
# Level 1: Syntax & Style
ruff check --fix && mypy .

# Level 2: Unit Tests
uv run pytest tests/ -v

# Level 3: Integration
uv run uvicorn main:app --reload
curl -X POST http://localhost:8000/endpoint -H "Content-Type: application/json" -d '{...}'

# Level 4: Deployment
# Custom validation as needed
```

## Development Workflow

### PRP Creation Process:
1. **Research Phase**: Deep codebase analysis and external research
2. **Context Gathering**: Collect all necessary documentation and examples
3. **Blueprint Design**: Create detailed implementation plan
4. **Validation Design**: Define executable validation gates
5. **Template Usage**: Use `PRPs/templates/prp_base.md` as starting point

### PRP Execution Process:
1. **Load PRP**: Read and understand all context and requirements
2. **Plan**: Create comprehensive implementation plan
3. **Execute**: Implement following the blueprint
4. **Validate**: Run each validation command, fix failures
5. **Complete**: Ensure all checklist items done, move to `PRPs/completed/`

## Code Quality Standards

### Anti-Patterns to Avoid:
- Don't create minimal context prompts - context is everything
- Don't skip validation steps - they're critical for one-pass success
- Don't ignore the structured PRP format - it's battle-tested
- Don't create new patterns when existing templates work
- Don't hardcode values that should be config
- Don't catch all exceptions - be specific

### File Organization:
```
PRPs-agentic-eng/
├── cursor_workflows/     # Cursor-specific workflows
├── PRPs/
│   ├── templates/        # PRP templates with validation
│   ├── scripts/         # PRP runner and utilities
│   ├── ai_docs/         # Curated documentation
│   ├── completed/       # Finished PRPs
│   └── *.md             # Active PRPs
├── claude_md_files/     # Framework examples
└── pyproject.toml       # Python configuration
```

## Development Commands

### PRP Execution:
```bash
# Interactive mode (recommended)
uv run PRPs/scripts/prp_runner.py --prp [name] --interactive --model cursor

# Headless mode
uv run PRPs/scripts/prp_runner.py --prp [name] --output-format json --model cursor
```

### Key Tools Available:
- **TodoWrite**: Create and track implementation plans
- **WebSearch**: Research documentation and examples
- **Agent**: Spawn subagents for parallel work
- **Edit/MultiEdit**: File editing capabilities
- **Bash**: Execute validation commands

## Best Practices

### When Creating PRPs:
- Include comprehensive context sections
- Reference existing codebase patterns
- Provide executable validation gates
- Use information-dense keywords
- Include error handling strategies

### When Executing PRPs:
- Follow the structured workflow
- Use subagents for parallel research
- Implement validation-first approach
- Test each component thoroughly
- Move completed PRPs to `PRPs/completed/`

## Template Usage
Always start with existing templates:
- `PRPs/templates/prp_base.md` - Comprehensive PRP template
- `PRPs/templates/prp_spec.md` - Specification template
- `PRPs/templates/prp_planning.md` - Planning template

## Success Metrics
Rate each PRP on a 1-10 scale for confidence in one-pass implementation success. Aim for 8+ through comprehensive context and validation.

Remember: The goal is **one-pass implementation success through comprehensive context and validation**. 