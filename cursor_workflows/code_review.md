# Code Review Workflow

## Purpose
Review code changes using PRP methodology principles for quality assurance.

## Usage
`@code_review.md [--staged] [--unstaged] [--all]`

## Review Process

### 1. Change Analysis
**Identify Changes:**
- Review git status to understand scope
- Examine staged vs unstaged changes
- Identify affected files and components
- Note any new dependencies or patterns

### 2. PRP Alignment Review
**Check PRP Compliance:**
- Verify changes align with PRP requirements
- Ensure all context considerations addressed
- Check that validation gates can still pass
- Confirm no deviation from implementation blueprint

### 3. Code Quality Assessment
**Standards Review:**
- Check adherence to existing patterns
- Verify proper error handling
- Ensure type hints are used appropriately
- Review for security considerations
- Check for hardcoded values that should be config

### 4. Implementation Review
**Technical Assessment:**
- Verify one component at a time approach
- Check progressive implementation pattern
- Ensure clear, maintainable code with comments
- Review for appropriate abstraction levels
- Check for potential regressions

### 5. Validation Review
**Test Coverage:**
- Verify all validation gates still pass
- Check that new functionality is testable
- Ensure integration tests cover new features
- Review error handling and edge cases
- Confirm no breaking changes

## Review Checklist

### Code Quality
- [ ] Follows existing code patterns
- [ ] Proper error handling implemented
- [ ] Type hints used appropriately
- [ ] No hardcoded configuration values
- [ ] Security considerations addressed
- [ ] Clear and maintainable code structure

### PRP Compliance
- [ ] All PRP requirements addressed
- [ ] Implementation follows blueprint
- [ ] No deviation from context guidelines
- [ ] Validation gates can still pass
- [ ] Edge cases handled as specified

### Testing
- [ ] All validation commands pass
- [ ] New functionality is testable
- [ ] Integration tests cover changes
- [ ] No regressions introduced
- [ ] Error paths properly tested

### Documentation
- [ ] Code comments are clear
- [ ] Any new patterns documented
- [ ] Breaking changes noted
- [ ] PRP updated if needed

## Review Commands
Execute these to validate changes:
```bash
# Syntax and style check
ruff check --fix && mypy .

# Unit tests
uv run pytest tests/ -v

# Git diff review
git diff --cached  # staged changes
git diff           # unstaged changes

# Security scan (if available)
# bandit -r src/

# Dependency check (if available)
# pip-audit
```

## Review Levels

### Level 1: Quick Review
- Check syntax and style
- Verify tests pass
- Review for obvious issues

### Level 2: Standard Review
- Full code quality assessment
- PRP compliance check
- Security considerations
- Performance implications

### Level 3: Deep Review
- Architecture impact analysis
- Integration testing
- Documentation review
- Regression testing

## Review Feedback Format
Provide feedback in this structure:
```
## Review Summary
- Overall assessment: [APPROVE/NEEDS_WORK/REJECT]
- Confidence level: [1-10]
- Risk level: [LOW/MEDIUM/HIGH]

## Findings
### Critical Issues
- [List any critical issues that must be fixed]

### Recommendations
- [List improvements and suggestions]

### Positive Aspects
- [List what was done well]

## Next Steps
- [List required actions before approval]
```

## Anti-Patterns to Flag
- Minimal context implementation
- Skipped validation steps
- Ignored structured format
- New patterns without justification
- Hardcoded values
- Generic exception handling
- Breaking changes without documentation

## Success Criteria
- All validation gates pass
- Code follows existing patterns
- PRP requirements fully met
- No regressions introduced
- Maintainable and secure code

## Example Usage
```
@code_review.md --staged
@code_review.md --all
```

Remember: **Review with the same rigor used in PRP creation - context is king, validation is critical.** 