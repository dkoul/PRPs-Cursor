# PRP Execution Workflow

## Purpose
Execute PRPs against the codebase to implement features with one-pass success.

## Usage
`@prp_execute.md <prp-file-path>`

## Workflow Steps

### 1. PRP Analysis
- Read and understand the complete PRP
- Analyze all context and requirements
- Identify key constraints and gotchas
- Note validation requirements

### 2. Planning Phase
**Create Implementation Plan:**
- Break down complex tasks into manageable steps
- Use TodoWrite to create and track implementation plan
- Identify implementation patterns from existing code
- Plan validation checkpoints

**Think Before You Code:**
- Understand the business context and user impact
- Consider error handling and edge cases
- Plan for type safety and security
- Review existing patterns to follow

### 3. Implementation Phase
**Follow Best Practices:**
- Implement one component at a time
- Follow code conventions from existing files
- Write clear, maintainable code with comments
- Use type hints for type safety
- Handle errors appropriately

**Progressive Implementation:**
- Start with core functionality
- Validate each component as you build
- Add features incrementally
- Test thoroughly at each step

### 4. Validation Phase
**Execute Validation Gates:**
Run each validation command from the PRP:
```bash
# Level 1: Syntax & Style
ruff check --fix && mypy .

# Level 2: Unit Tests
uv run pytest tests/ -v

# Level 3: Integration Tests
# Custom validation from PRP

# Level 4: Deployment Tests
# Custom validation from PRP
```

**Fix Issues:**
- Address any validation failures
- Iterate until all gates pass
- Verify all requirements satisfied

### 5. Completion
**Final Checks:**
- Ensure all PRP requirements met
- Run full validation suite
- Verify no regressions introduced
- Test edge cases and error conditions

**Cleanup:**
- Move completed PRP to `PRPs/completed/`
- Update any relevant documentation
- Commit changes with clear message

## Implementation Approach Example
1. **Analyze** the PRP requirements in detail
2. **Search** for existing patterns in the codebase
3. **Research** additional context and examples via WebSearch
4. **Plan** step-by-step implementation with TodoWrite
5. **Implement** core functionality first, then additional features
6. **Validate** each component thoroughly
7. **Complete** when all validation gates pass

## Success Criteria
- All PRP requirements implemented
- All validation gates pass
- Code follows existing patterns
- No regressions introduced
- PRP moved to completed folder

## Example Usage
```
@prp_execute.md PRPs/user-authentication.md
```

## Tools Available
- **TodoWrite**: Track implementation progress
- **WebSearch**: Research additional context
- **Agent**: Spawn subagents for parallel work
- **Edit/MultiEdit**: File editing capabilities
- **Bash**: Execute validation commands
- **Read/Grep**: Examine existing code patterns

Remember: **Output "DONE" when all tests pass and the PRP is fully implemented.** 