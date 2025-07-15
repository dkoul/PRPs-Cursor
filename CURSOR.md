# CURSOR.md

This file provides guidance to Cursor when working with code in this repository.

## Project Nature

This is a **PRP (Product Requirement Prompt) Framework** repository, not a traditional software project. The core concept: **"PRP = PRD + curated codebase intelligence + agent/runbook"** - designed to enable AI agents to ship production-ready code on the first pass.

## Core Architecture

### Workflow-Driven System

- **Cursor workflows** in `cursor_workflows/` directory
- Workflows organized by function:
  - `prp_create.md` - Create comprehensive PRPs with research
  - `prp_execute.md` - Execute PRPs against codebase
  - `prime_context.md` - Load project context
  - `code_review.md` - Review code changes using PRP methodology

### Template-Based Methodology

- **PRP Templates** in `PRPs/templates/` follow structured format with validation loops
- **Context-Rich Approach**: Every PRP must include comprehensive documentation, examples, and gotchas
- **Validation-First Design**: Each PRP contains executable validation gates (syntax, tests, integration)

### AI Documentation Curation

- `PRPs/ai_docs/` contains curated documentation for context injection
- `claude_md_files/` provides framework-specific examples

## Development Commands

### PRP Execution

```bash
# Interactive mode with Cursor (recommended)
uv run PRPs/scripts/prp_runner.py --prp [prp-name] --interactive --model cursor

# Headless mode with Claude Code
uv run PRPs/scripts/prp_runner.py --prp [prp-name] --output-format json --model claude

# Streaming JSON with Claude Code
uv run PRPs/scripts/prp_runner.py --prp [prp-name] --output-format stream-json --model claude
```

### Key Cursor Workflows

- `@prime_context.md` - Load project context and understand PRP methodology
- `@prp_create.md <feature>` - Generate comprehensive PRPs with research
- `@prp_execute.md <prp-file>` - Execute PRPs against codebase
- `@code_review.md` - Review code changes using PRP methodology

## Critical Success Patterns

### The PRP Methodology

1. **Context is King**: Include ALL necessary documentation, examples, and caveats
2. **Validation Loops**: Provide executable tests/lints the AI can run and fix
3. **Information Dense**: Use keywords and patterns from the codebase
4. **Progressive Success**: Start simple, validate, then enhance

### PRP Structure Requirements

- **Goal**: Specific end state and desires
- **Why**: Business value and user impact
- **What**: User-visible behavior and technical requirements
- **All Needed Context**: Documentation URLs, code examples, gotchas, patterns
- **Implementation Blueprint**: Pseudocode with critical details and task lists
- **Validation Loop**: Executable commands for syntax, tests, integration

### Validation Gates (Must be Executable)

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

## Anti-Patterns to Avoid

- ❌ Don't create minimal context prompts - context is everything
- ❌ Don't skip validation steps - they're critical for one-pass success
- ❌ Don't ignore the structured PRP format - it's battle-tested
- ❌ Don't create new patterns when existing templates work
- ❌ Don't hardcode values that should be config
- ❌ Don't catch all exceptions - be specific

## Working with This Framework

### When Creating new PRPs

1. **Start with `@prime_context.md`** to understand the project
2. **Use `@prp_create.md <feature>`** to generate comprehensive PRPs
3. **Follow the research process**: Deep codebase analysis + external research
4. **Include comprehensive context**: URLs, examples, gotchas, patterns
5. **Design executable validation gates**
6. **Score confidence level 1-10** (aim for 8+)

### When Executing PRPs

1. **Use `@prp_execute.md <prp-file>`** to implement features
2. **Follow the structured workflow**:
   - Load PRP and understand context
   - Plan implementation approach
   - Execute progressively
   - Validate continuously
   - Complete when all gates pass
3. **Move completed PRPs to `PRPs/completed/`**

### Code Review Process

1. **Use `@code_review.md`** for reviewing changes
2. **Check PRP compliance** and validation gates
3. **Verify no regressions** and pattern adherence
4. **Ensure comprehensive testing**

## Project Structure Understanding

```
PRPs-agentic-eng/
├── .cursorrules           # Cursor-specific rules and guidelines
├── cursor_workflows/      # Cursor workflows for PRP methodology
│   ├── prp_create.md      # Create comprehensive PRPs
│   ├── prp_execute.md     # Execute PRPs against codebase
│   ├── prime_context.md   # Load project context
│   └── code_review.md     # Review code changes
├── PRPs/
│   ├── templates/         # PRP templates with validation
│   ├── scripts/          # PRP runner (supports both Cursor and Claude)
│   ├── ai_docs/          # Curated documentation
│   ├── completed/        # Finished PRPs
│   └── *.md              # Active PRPs
├── claude_md_files/       # Framework-specific examples
├── CURSOR.md             # This file - Cursor-specific guidance
└── pyproject.toml        # Python package configuration
```

## Cursor-Specific Features

### Workflow Integration

- **@-mentions**: Use `@prime_context.md`, `@prp_create.md`, etc.
- **Context Loading**: Cursor automatically loads project context
- **Interactive Development**: Real-time implementation with validation
- **File Management**: Automatic file creation and organization

### Development Flow

1. **Prime Context**: `@prime_context.md` to understand the project
2. **Create PRP**: `@prp_create.md <feature>` for new features
3. **Execute PRP**: `@prp_execute.md <prp-file>` for implementation
4. **Review Code**: `@code_review.md` for quality assurance
5. **Validate**: Run validation gates throughout

### Tools Available

- **File Editing**: Direct file manipulation capabilities
- **Terminal Access**: Run validation commands and tests
- **Codebase Search**: Find existing patterns and conventions
- **Web Search**: Research documentation and examples
- **Todo Management**: Track implementation progress

## Success Metrics

- **Confidence Score**: Rate each PRP 1-10 for one-pass success (aim for 8+)
- **Validation Gates**: All must pass before completion
- **Pattern Adherence**: Follow existing codebase conventions
- **No Regressions**: Ensure existing functionality unchanged
- **Documentation**: Clear, comprehensive context provided

## Best Practices

### PRP Creation
- Start with comprehensive research
- Include all necessary context
- Design executable validation gates
- Reference existing patterns
- Aim for 8+ confidence score

### PRP Execution
- Follow structured workflow
- Implement progressively
- Validate continuously
- Use available tools effectively
- Test thoroughly

### Code Review
- Check PRP compliance
- Verify validation gates pass
- Ensure pattern adherence
- Test for regressions
- Maintain code quality

Remember: This framework is about **one-pass implementation success through comprehensive context and validation**. Every PRP should contain the exact context for an AI agent to successfully implement working code in a single pass.

## Migration from Claude Code

This project has been refactored to work with Cursor while maintaining compatibility with Claude Code:

- **Cursor workflows** replace Claude Code commands
- **PRP runner** supports both `--model cursor` and `--model claude`
- **Documentation** updated for Cursor-specific features
- **Templates** remain compatible with both systems

Use `--model cursor` for interactive development with Cursor, or `--model claude` for headless execution with Claude Code. 