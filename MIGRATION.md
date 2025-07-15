# Migration Guide: Claude Code to Cursor

This guide helps you transition from using Claude Code commands to Cursor workflows while maintaining all PRP functionality.

## What Changed

### Before (Claude Code)
- Used `.claude/commands/` directory with slash commands
- Commands like `/create-base-prp`, `/execute-base-prp`, `/prime-core`
- Required Claude Code CLI installation
- Headless and interactive modes supported

### After (Cursor + Claude Code)
- Uses `cursor_workflows/` directory with @ workflows
- Workflows like `@prp_create.md`, `@prp_execute.md`, `@prime_context.md`
- Works with Cursor (primary) and Claude Code (compatibility)
- Interactive development with real-time validation

## Migration Steps

### 1. New File Structure
```bash
# Old structure
.claude/
├── commands/
│   ├── PRPs/
│   ├── development/
│   └── ...

# New structure
.cursorrules                 # Cursor-specific rules
cursor_workflows/            # Cursor workflows
├── prp_create.md
├── prp_execute.md
├── prime_context.md
└── code_review.md
PRPs/completed/              # New: completed PRPs folder
```

### 2. Command → Workflow Mapping

| Claude Code Command | Cursor Workflow | Purpose |
|-------------------|----------------|---------|
| `/create-base-prp` | `@prp_create.md` | Create comprehensive PRPs |
| `/execute-base-prp` | `@prp_execute.md` | Execute PRPs against codebase |
| `/prime-core` | `@prime_context.md` | Load project context |
| `/review-staged-unstaged` | `@code_review.md` | Review code changes |

### 3. Usage Changes

**Before (Claude Code):**
```bash
# In Claude Code interface
/create-base-prp user authentication system
/execute-base-prp PRPs/user-auth.md
/prime-core
```

**After (Cursor):**
```bash
# In Cursor interface
@prp_create.md user authentication system
@prp_execute.md PRPs/user-auth.md
@prime_context.md
```

### 4. PRP Runner Changes

**Before:**
```bash
# Only supported Claude Code
uv run PRPs/scripts/prp_runner.py --prp my-feature --interactive
```

**After:**
```bash
# Cursor (recommended)
uv run PRPs/scripts/prp_runner.py --prp my-feature --interactive --model cursor

# Claude Code (still supported)
uv run PRPs/scripts/prp_runner.py --prp my-feature --interactive --model claude
```

## Key Benefits of Migration

### 1. Better Integration
- Native Cursor integration with @ workflows
- Real-time file editing and validation
- Seamless codebase navigation

### 2. Enhanced Development Experience
- Interactive development with immediate feedback
- Built-in project context loading
- Streamlined workflow execution

### 3. Maintained Compatibility
- All existing PRPs work unchanged
- Claude Code still supported for CI/CD
- Templates remain compatible

### 4. Improved Validation
- Real-time validation gate execution
- Better error handling and feedback
- Progressive implementation support

## Migration Checklist

### For Existing Projects
- [ ] Copy `.cursorrules` to project root
- [ ] Copy `cursor_workflows/` directory
- [ ] Create `PRPs/completed/` directory
- [ ] Update `CLAUDE.md` → `CURSOR.md`
- [ ] Test workflows with sample PRP

### For New Projects
- [ ] Start with Cursor-first approach
- [ ] Use `@prime_context.md` to understand project
- [ ] Create PRPs with `@prp_create.md`
- [ ] Execute PRPs with `@prp_execute.md`
- [ ] Review code with `@code_review.md`

## Troubleshooting

### Common Issues

**1. Workflow not recognized:**
```bash
# Make sure workflows are in cursor_workflows/ directory
# Use @ prefix: @prp_create.md not prp_create.md
```

**2. Model not working:**
```bash
# Check model flag in runner
uv run PRPs/scripts/prp_runner.py --prp test --model cursor --interactive
```

**3. Temporary files left behind:**
```bash
# Runner cleans up temp_prp_session.md automatically
# Check .gitignore includes temp_prp_session.md
```

### Getting Help

1. **Start with context**: Always run `@prime_context.md` first
2. **Check workflows**: Ensure workflows are in `cursor_workflows/`
3. **Validate setup**: Test with simple PRP execution
4. **Fallback to Claude**: Use `--model claude` if needed

## Backward Compatibility

The migration maintains full backward compatibility:

### Claude Code Commands
- All original commands still work
- Use `.claude/commands/` structure
- Headless mode with JSON output supported

### Existing PRPs
- No changes needed to existing PRPs
- All templates work with both systems
- Validation gates remain the same

### CI/CD Integration
- Use Claude Code for automated execution
- JSON output for parsing results
- Streaming JSON for real-time monitoring

## Example Migration

### Before: Claude Code Project
```bash
project/
├── .claude/
│   └── commands/
├── PRPs/
│   ├── templates/
│   ├── scripts/
│   └── feature.md
└── CLAUDE.md
```

### After: Cursor + Claude Code Project
```bash
project/
├── .cursorrules
├── cursor_workflows/
│   ├── prp_create.md
│   ├── prp_execute.md
│   ├── prime_context.md
│   └── code_review.md
├── .claude/                    # Optional: keep for CI/CD
│   └── commands/
├── PRPs/
│   ├── templates/
│   ├── scripts/
│   ├── completed/             # New: for finished PRPs
│   └── feature.md
├── CURSOR.md                  # Replaces CLAUDE.md
└── CLAUDE.md                  # Optional: keep for reference
```

## Next Steps

1. **Test the migration** with a sample PRP
2. **Train your team** on new workflows
3. **Update documentation** to reference Cursor
4. **Gradually phase out** Claude Code commands
5. **Leverage Cursor features** for enhanced development

Remember: The goal remains the same - **one-pass implementation success through comprehensive context**. The migration just makes it easier to achieve! 