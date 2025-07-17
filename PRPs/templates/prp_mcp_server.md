name: "MCP Server PRP Template - Context-Rich Implementation Guide"
description: |
  Template for implementing custom MCP (Model Context Protocol) servers with FastMCP framework,
  containerization, and proper tool definitions for AI agent integration.

## Purpose

Template optimized for AI agents to implement custom MCP servers that expose external APIs and services 
to AI tools through the Model Context Protocol, with complete context for successful first-pass implementation.

## Core Principles

1. **FastMCP Framework**: Use FastMCP for rapid MCP server development
2. **Tool-First Design**: Define clear, focused tools with proper descriptions
3. **Environment Configuration**: Externalize all configuration via environment variables
4. **Container Ready**: Include containerization for easy deployment
5. **Validation Loops**: Provide executable tests for MCP protocol compliance

---

## Goal

[What MCP server needs to be built - be specific about the external service/API it will expose and what tools it will provide]

Example: "Build an MCP server that exposes GitHub API functionality through standardized tools for repository management, issue tracking, and code search."

## Why

- [Business value of exposing this service through MCP]
- [Which AI workflows this will enable]
- [Integration benefits with existing MCP ecosystem]
- [Problems this solves for AI agents and users]

## What

[Specific tools and functionality the MCP server will provide]

### Success Criteria

- [ ] MCP server implements required tools with proper schemas
- [ ] Server handles authentication and rate limiting appropriately
- [ ] Container builds and runs successfully
- [ ] Tools respond correctly to MCP protocol requests
- [ ] Error handling provides meaningful feedback to AI agents

## All Needed Context

### Documentation & References

```yaml
# MUST READ - Include these in your context window
- url: https://spec.modelcontextprotocol.io/
  why: MCP protocol specification and compliance requirements
  critical: Tool schema definitions and response formats

- url: https://github.com/pydantic/fastmcp
  why: FastMCP framework documentation and examples
  critical: Tool decorators and server lifecycle management

- url: [External API Documentation URL]
  why: Understanding endpoints, authentication, rate limits
  critical: Request/response schemas and error codes

- file: PRPs-Cursor/mcp-server-template/mcp_server.py
  why: Reference implementation pattern for FastMCP servers
  critical: HTTP client setup and tool definition patterns

- doc: https://docs.docker.com/engine/reference/builder/
  section: Multi-stage builds and Python optimization
  critical: Container optimization for MCP servers
```

### Current Codebase tree (for new MCP server project)

```bash
# Expected starting point - empty directory or basic Python project
./
├── README.md (optional)
└── .git/ (if version controlled)
```

### Desired Codebase tree with files to be added

```bash
mcp-[server-name]/
├── mcp_server.py           # Main MCP server implementation
├── requirements.txt        # Python dependencies
├── Containerfile          # Container build instructions  
├── README.md              # Setup and usage documentation
├── .env.example           # Environment variable template
├── tests/
│   ├── __init__.py
│   ├── test_server.py     # MCP server tests
│   └── test_tools.py      # Individual tool tests
└── config/
    └── settings.py        # Configuration management
```

### Known Gotchas & MCP/FastMCP Quirks

```python
# CRITICAL: FastMCP tool functions must be async
@mcp.tool()
async def my_tool():  # ✅ Correct
    pass

def my_tool():        # ❌ Will fail at runtime
    pass

# CRITICAL: Tool descriptions are mandatory and must be detailed
@mcp.tool()
async def search_repos():
    """Search GitHub repositories."""  # ❌ Too brief
    pass

@mcp.tool()
async def search_repos(query: str, sort: str = "updated"):
    """Search GitHub repositories by query string.
    
    Args:
        query: Search terms (supports GitHub search syntax)
        sort: Sort order (updated, stars, forks, created)
    
    Returns:
        List of repository objects with name, description, URL, stats
    """  # ✅ Detailed and helpful
    pass

# CRITICAL: MCP transport must be configured via environment
mcp.run(transport=os.environ.get("MCP_TRANSPORT", "stdio"))  # ✅
mcp.run()  # ❌ Missing transport configuration

# CRITICAL: HTTP client should use connection pooling
async with httpx.AsyncClient() as client:  # ✅ Per-request client
    response = await client.get(url)

client = httpx.AsyncClient()  # ❌ Global client without proper cleanup

# CRITICAL: Error handling must provide actionable feedback
try:
    response = await client.request(method, url)
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    if e.response.status_code == 401:
        raise ValueError("Invalid API key - check API_KEY environment variable")
    elif e.response.status_code == 429:
        raise ValueError("Rate limit exceeded - please retry after delay")
    else:
        raise ValueError(f"API error {e.response.status_code}: {e.response.text}")
```

## Implementation Blueprint

### Data models and structure

Define Pydantic models for API responses and tool parameters to ensure type safety.

```python
from pydantic import BaseModel, Field
from typing import List, Optional

class ToolParameter(BaseModel):
    query: str = Field(..., description="Search query string")
    limit: int = Field(10, description="Maximum number of results", ge=1, le=100)
    
class APIResponse(BaseModel):
    success: bool
    data: Optional[dict] = None
    error: Optional[str] = None
    
class ToolResult(BaseModel):
    """Standardized tool response format"""
    status: str  # "success" | "error" 
    message: str
    data: Optional[dict] = None
```

### List of tasks to be completed

```yaml
Task 1 - Project Setup:
CREATE mcp_server.py:
  - IMPORT FastMCP, httpx, os, typing
  - SETUP mcp = FastMCP("[server-name]")
  - DEFINE environment variables (API_BASE_URL, API_KEY, etc.)

CREATE requirements.txt:
  - INCLUDE fastmcp, httpx, pydantic
  - ADD any external API SDKs if needed

Task 2 - HTTP Client Implementation:
IMPLEMENT make_request function in mcp_server.py:
  - MIRROR pattern from: mcp-server-template/mcp_server.py
  - ADD proper error handling for HTTP status codes
  - INCLUDE authentication headers if required
  - HANDLE rate limiting and retries

Task 3 - Core Tools Implementation:
CREATE @mcp.tool() decorated functions:
  - DEFINE [3-5 essential tools] for the target service
  - INCLUDE comprehensive docstrings with Args/Returns
  - IMPLEMENT proper parameter validation
  - RETURN structured responses

Task 4 - Configuration Management:
CREATE config/settings.py:
  - CENTRALIZE environment variable handling
  - PROVIDE validation for required variables
  - INCLUDE default values where appropriate

Task 5 - Error Handling:
IMPLEMENT comprehensive error handling:
  - HTTP errors (401, 429, 500, etc.)
  - Network timeouts and connection issues
  - Invalid API responses
  - Missing environment variables

Task 6 - Containerization:
CREATE Containerfile:
  - MIRROR pattern from: mcp-server-template/Containerfile
  - USE Python 3.11+ base image
  - OPTIMIZE for container size and security

Task 7 - Documentation:
CREATE README.md:
  - INCLUDE setup instructions
  - DOCUMENT environment variables
  - PROVIDE example MCP client configuration
  - ADD troubleshooting section

Task 8 - Testing:
CREATE test suite:
  - Unit tests for individual tools
  - Integration tests with mock API responses
  - MCP protocol compliance tests
```

### Core Tools Pseudocode

```python
# Example tool implementation pattern
@mcp.tool()
async def search_items(query: str, category: str = "all") -> dict:
    """Search items in the external service.
    
    Args:
        query: Search terms to find relevant items
        category: Filter by category (all, type1, type2)
    
    Returns:
        Dictionary with search results and metadata
    """
    # PATTERN: Validate inputs first
    if not query.strip():
        return {"status": "error", "message": "Query cannot be empty"}
    
    # PATTERN: Build API request
    url = f"{API_BASE_URL}/search"
    params = {"q": query, "category": category}
    
    try:
        # CRITICAL: Use the shared HTTP client pattern
        response = await make_request(url, method="GET", data=params)
        
        # PATTERN: Transform API response to tool format
        return {
            "status": "success",
            "message": f"Found {len(response.get('items', []))} items",
            "data": {
                "items": response.get("items", []),
                "total": response.get("total", 0),
                "query": query
            }
        }
    except Exception as e:
        # PATTERN: Return structured error
        return {
            "status": "error", 
            "message": f"Search failed: {str(e)}",
            "data": None
        }

# Additional tools following same pattern...
@mcp.tool()
async def get_item_details(item_id: str) -> dict:
    """Get detailed information about a specific item."""
    # Implementation following same patterns...

@mcp.tool() 
async def create_item(name: str, description: str) -> dict:
    """Create a new item in the service."""
    # Implementation following same patterns...
```

### Integration Points

```yaml
ENVIRONMENT:
  - required: "API_BASE_URL, API_KEY, MCP_TRANSPORT"
  - optional: "REQUEST_TIMEOUT=30, MAX_RETRIES=3"
  - validation: "Fail fast if required vars missing"

MCP_CLIENT_CONFIG:
  - transport: "stdio (default) or sse"
  - security: "Sandbox if needed for external API calls"
  - timeout: "Configure based on API response times"

EXTERNAL_API:
  - authentication: "Bearer token via API_KEY header"
  - rate_limits: "Respect API rate limits in make_request"
  - endpoints: "Map to intuitive MCP tool names"
```

## Validation Loop

### Level 1: Syntax & Style

```bash
# Run these FIRST - fix any errors before proceeding
python -m py_compile mcp_server.py     # Basic syntax check
pip install -r requirements.txt       # Install dependencies

# If using additional linting:
# ruff check mcp_server.py --fix
# mypy mcp_server.py

# Expected: No syntax errors, clean imports
```

### Level 2: MCP Server Startup

```bash
# Test basic server startup
export API_BASE_URL="https://api.example.com"
export API_KEY="test_key_for_validation"
export MCP_TRANSPORT="stdio"

python mcp_server.py &
SERVER_PID=$!

# Expected: Server starts without immediate errors
# Kill test server: kill $SERVER_PID
```

### Level 3: Tool Testing

```python
# CREATE test_tools.py - test individual tools with mock responses
import pytest
from unittest.mock import patch, AsyncMock
from mcp_server import search_items, get_item_details

@pytest.mark.asyncio
async def test_search_items_success():
    """Test successful search returns formatted results"""
    mock_response = {
        "items": [{"id": "1", "name": "Test Item"}],
        "total": 1
    }
    
    with patch('mcp_server.make_request', return_value=mock_response):
        result = await search_items("test query")
        
    assert result["status"] == "success"
    assert result["data"]["total"] == 1
    assert len(result["data"]["items"]) == 1

@pytest.mark.asyncio
async def test_search_items_empty_query():
    """Test validation catches empty queries"""
    result = await search_items("")
    assert result["status"] == "error"
    assert "empty" in result["message"].lower()

# Run tests:
# pytest test_tools.py -v
```

### Level 4: MCP Protocol Integration

```bash
# Test with actual MCP client (Claude Desktop or compatible)
# 1. Build container
podman build -t mcp-[server-name]:latest .

# 2. Test container runs
podman run -i --rm \
  -e API_BASE_URL="https://api.example.com" \
  -e API_KEY="your_test_key" \
  -e MCP_TRANSPORT="stdio" \
  localhost/mcp-[server-name]:latest

# 3. Validate MCP client configuration
# Add to MCP client config and test tool invocation:
{
  "mcpServers": {
    "[server-name]": {
      "command": "podman",
      "args": ["run", "-i", "--rm", 
               "-e", "API_BASE_URL", 
               "-e", "API_KEY",
               "-e", "MCP_TRANSPORT",
               "localhost/mcp-[server-name]:latest"],
      "env": {
        "API_BASE_URL": "https://api.example.com",
        "API_KEY": "your_api_key",
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}

# Expected: Tools appear in MCP client and respond correctly
```

## Final Validation Checklist

- [ ] Server starts without errors: `python mcp_server.py`
- [ ] All tools have comprehensive docstrings with Args/Returns
- [ ] Container builds successfully: `podman build -t mcp-server .`
- [ ] Container runs with env vars: `podman run -i --rm -e API_KEY=test mcp-server`
- [ ] Tools handle errors gracefully (network, auth, validation)
- [ ] MCP client can discover and invoke tools
- [ ] API rate limits and timeouts are respected
- [ ] README.md provides clear setup instructions

---

## Anti-Patterns to Avoid

- ❌ Don't create sync functions - FastMCP requires async tools
- ❌ Don't skip tool docstrings - they're critical for AI understanding  
- ❌ Don't hardcode API URLs or keys - use environment variables
- ❌ Don't ignore HTTP error codes - handle 401, 429, 500 specifically
- ❌ Don't use global HTTP clients - prefer async context managers
- ❌ Don't return raw API responses - transform to consistent format
- ❌ Don't skip container testing - MCP servers often run containerized
- ❌ Don't forget MCP_TRANSPORT configuration - required for deployment

---

## Example External Services for MCP Integration

- **GitHub API**: Repository management, issues, code search
- **Slack API**: Message posting, channel management, user lookup  
- **Notion API**: Page creation, database queries, content search
- **Jira API**: Issue tracking, project management, reporting
- **AWS APIs**: Resource management, monitoring, deployment
- **Database APIs**: Query execution, schema introspection, data analysis 