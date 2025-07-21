# How to Use the PRP Framework with Cursor

## Overview
This guide shows you how to use the refactored PRP framework with Cursor for one-pass implementation success.

## 🎯 Core Workflow

### Step 1: Prime Your Context
**Always start here** to understand the project:
```
@prime_context.md
```

**What this does:**
- Loads project structure and PRP methodology
- Explains available templates and workflows
- Sets up your understanding of the codebase

### Step 2: Create a Comprehensive PRP
Generate a detailed PRP with research:
```
@prp_create.md implement user dashboard with real-time updates
```

**What this does:**
- Researches similar patterns in codebase
- Searches for external documentation and examples
- Creates comprehensive context with gotchas and best practices
- Designs executable validation gates
- Generates implementation blueprint

### Step 3: Execute the PRP
Implement the feature following the PRP:
```
@prp_execute.md PRPs/user-dashboard.md
```

**What this does:**
- Loads PRP context and requirements
- Creates step-by-step implementation plan
- Implements progressively with validation
- Runs validation gates continuously
- Moves completed PRP to PRPs/completed/

### Step 4: Review Your Work
Review changes using PRP methodology:
```
```

**What this does:**
- Checks PRP compliance
- Validates all gates pass
- Ensures no regressions
- Verifies pattern adherence

## 🛠️ Alternative: Command Line Usage

### For Interactive Development (Recommended)
```bash
# Cursor interactive mode
uv run PRPs/scripts/prp_runner.py --prp my-feature --interactive --model cursor
```

### For CI/CD and Headless Execution
```bash
# Claude Code headless mode
uv run PRPs/scripts/prp_runner.py --prp my-feature --output-format json --model claude

# With streaming output
uv run PRPs/scripts/prp_runner.py --prp my-feature --output-format stream-json --model claude
```

## 📝 Complete Example Walkthrough

### Scenario: Adding User Authentication

**1. Prime Context**
```
@prime_context.md
```
*Output: Understanding of project structure, PRP methodology, available templates*

**2. Create PRP**
```
@prp_create.md user authentication system with JWT tokens and refresh tokens
```
*Output: `PRPs/user-auth.md` with comprehensive context, validation gates, and implementation plan*

**3. Execute PRP**
```
@prp_execute.md PRPs/user-auth.md
```
*Output: Complete implementation with tests, validation passed, PRP moved to completed/*

**4. Review Changes**
```
@code_review.md
```
*Output: Quality assessment, validation confirmation, approval for merge*

## 🎨 Manual PRP Creation (Alternative)

If you prefer to create PRPs manually:

### 1. Use Template
```bash
cp PRPs/templates/prp_base.md PRPs/my-feature.md
```

### 2. Fill Required Sections
- **Goal**: What needs to be built
- **Why**: Business value and user impact
- **What**: Technical requirements and success criteria
- **All Needed Context**: Documentation, examples, gotchas
- **Implementation Blueprint**: Step-by-step plan
- **Validation Loop**: Executable commands

### 3. Execute with Cursor
```
@prp_execute.md PRPs/my-feature.md
```

## 📊 Understanding PRP Quality

### Success Metrics
- **Confidence Score**: Rate 1-10 for one-pass success (aim for 8+)
- **Context Completeness**: All necessary info included
- **Validation Gates**: All must be executable
- **Pattern Adherence**: Follows existing codebase conventions

### Quality Checklist
- [ ] All necessary context included
- [ ] Validation gates are executable
- [ ] References existing patterns
- [ ] Clear implementation path
- [ ] Error handling documented
- [ ] Comprehensive research completed

## 🔄 Advanced Usage

### Multiple PRPs in Parallel
```bash
# Create multiple features
@prp_create.md user authentication system
@prp_create.md email notification service
@prp_create.md payment processing integration

# Execute in parallel using Git worktrees
git worktree add -b feature-auth ../project-auth
git worktree add -b feature-email ../project-email
git worktree add -b feature-payment ../project-payment
```

### Custom Validation Gates
Add project-specific validation to your PRPs:
```bash
# Example validation gates
ruff check --fix && mypy .              # Syntax & Style
uv run pytest tests/ -v                 # Unit Tests
uv run pytest tests/integration/ -v     # Integration Tests
curl -f http://localhost:8000/health     # Health Check
docker build -t myapp .                 # Build Test
```

### Integration with CI/CD
```yaml
# GitHub Actions example
name: Execute PRP
on:
  push:
    paths: ['PRPs/*.md']

jobs:
  execute-prp:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install UV
        run: pip install uv
      - name: Execute PRP
        run: |
          uv run PRPs/scripts/prp_runner.py \
            --prp ${{ github.event.head_commit.message }} \
            --output-format json \
            --model claude > result.json
      - name: Upload Results
        uses: actions/upload-artifact@v3
        with:
          name: prp-execution-results
          path: result.json
```

## 🆘 Troubleshooting

### Common Issues

**1. Workflow not recognized**
```bash
# Ensure @ prefix is used
✅ @prime_context.md
❌ prime_context.md
```

**2. PRP not found**
```bash
# Check file exists
ls PRPs/my-feature.md

# Use correct path
@prp_execute.md PRPs/my-feature.md
```

**3. Validation gates failing**
```bash
# Run validation manually
ruff check --fix && mypy .
uv run pytest tests/ -v

# Check PRP for correct validation commands
```

**4. Model issues**
```bash
# Use correct model flag
uv run PRPs/scripts/prp_runner.py --prp test --model cursor --interactive
```

### Getting Help

1. **Start with context**: `@prime_context.md`
2. **Check documentation**: Read `CURSOR.md` and `MIGRATION.md`
3. **Test with simple PRP**: Use existing example
4. **Fallback to Claude**: Use `--model claude` if needed

## 🎯 Best Practices

### For PRP Creation
- Always start with `@prime_context.md`
- Include comprehensive research and context
- Design executable validation gates
- Reference existing codebase patterns
- Aim for 8+ confidence score

### For PRP Execution
- Follow the structured workflow
- Implement progressively
- Validate continuously
- Test thoroughly
- Move completed PRPs to `PRPs/completed/`

### For Code Review
- Check PRP compliance
- Verify all validation gates pass
- Ensure no regressions
- Maintain code quality standards

## 📈 Success Metrics

### Individual PRP Success
- All validation gates pass
- Implementation matches PRP requirements
- No regressions introduced
- Code follows existing patterns

### Team Success
- Consistent PRP usage across team
- High confidence scores (8+)
- Reduced implementation time
- Fewer bugs and rework cycles

Remember: **The goal is one-pass implementation success through comprehensive context.** Use the workflows, follow the methodology, and validate continuously!

## 🔗 Quick Reference

| Task | Command |
|------|---------|
| Load context | `@prime_context.md` |
| Create PRP | `@prp_create.md <feature>` |
| Execute PRP | `@prp_execute.md <prp-file>` |
| Review code | `@code_review.md` |
| Run with Cursor | `--model cursor --interactive` |
| Run with Claude | `--model claude --output-format json` |

Start with `@prime_context.md` and you're ready to go! 🚀 