# PRP Creation Workflow

## Purpose
Create comprehensive PRPs with deep research to enable one-pass implementation success.

## Usage
`@prp_create.md <feature-description>`

## Workflow Steps

### 1. Initial Analysis
- Analyze the feature request in detail
- Identify key requirements and constraints
- Determine scope and complexity

### 2. Research Phase
**Deep Codebase Analysis:**
- Search for similar features/patterns in the codebase
- Identify all necessary files to reference
- Note existing conventions and patterns
- Check test patterns for validation approach
- Use TodoWrite to track research findings

**External Research:**
- Search for library documentation (include specific URLs)
- Find implementation examples (GitHub/StackOverflow/blogs)
- Identify best practices and common pitfalls
- For critical documentation, add .md files to `PRPs/ai_docs/`

### 3. Context Gathering
Collect and organize:
- **Documentation URLs** with specific sections
- **Code Examples** from the codebase
- **Gotchas** and library quirks
- **Patterns** to follow
- **Best Practices** from research

### 4. PRP Generation
Using `PRPs/templates/prp_base.md` as template:

**Required Sections:**
- Goal: Specific end state
- Why: Business value and impact
- What: User-visible behavior and technical requirements
- All Needed Context: Comprehensive documentation and examples
- Implementation Blueprint: Detailed pseudocode and task list
- Validation Loop: Executable validation commands

**Critical Context to Include:**
- Documentation URLs with specific sections
- Real code snippets from codebase
- Library quirks and version issues
- Existing patterns to follow
- Common pitfalls found during research

### 5. Validation Gates Design
Create executable validation commands:
```bash
# Syntax/Style
ruff check --fix && mypy .

# Unit Tests
uv run pytest tests/ -v

# Integration Tests
# Custom validation as needed

# Deployment Tests
# Custom validation as needed
```

### 6. Quality Assurance
**Quality Checklist:**
- [ ] All necessary context included
- [ ] Validation gates are executable
- [ ] References existing patterns
- [ ] Clear implementation path
- [ ] Error handling documented
- [ ] Comprehensive research completed

**Score the PRP** on a scale of 1-10 for confidence in one-pass implementation success.

### 7. Output
Save as: `PRPs/{feature-name}.md`

## Example Usage
```
@prp_create.md user authentication system with JWT tokens
```

## Success Criteria
- PRP contains comprehensive context for one-pass implementation
- Validation gates are executable by AI agents
- References existing codebase patterns
- Includes error handling and edge cases
- Scores 8+ on confidence scale

Remember: **The goal is one-pass implementation success through comprehensive context.** 