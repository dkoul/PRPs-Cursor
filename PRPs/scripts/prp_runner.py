#!/usr/bin/env -S uv run --script
"""Run an AI coding agent against a PRP.

KISS version - no repo-specific assumptions.

Optimized for Cursor development environment.

Typical usage:
    uv run PRPs/scripts/prp_runner.py --prp test --interactive
    uv run PRPs/scripts/prp_runner.py --prp test

Arguments:
    --prp-path       Path to a PRP markdown file (overrides --prp)
    --prp            Feature key; resolves to PRPs/{feature}.md
    --interactive    Run in interactive mode; otherwise headless text output
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # project root

META_HEADER = """Ingest and understand the Product Requirement Prompt (PRP) below in detail.

    # WORKFLOW GUIDANCE:

    ## Planning Phase
    - Think hard before you code. Create a comprehensive plan addressing all requirements.
    - Break down complex tasks into smaller, manageable steps.
    - Use the TodoWrite tool to create and track your implementation plan.
    - Identify implementation patterns from existing code to follow.

    ## Implementation Phase
    - Follow code conventions and patterns found in existing files.
    - Implement one component at a time and verify it works correctly.
    - Write clear, maintainable code with appropriate comments.
    - Consider error handling, edge cases, and potential security issues.
    - Use type hints to ensure type safety.

    ## Validation Phase
    - Run all validation commands specified in the PRP.
    - Test the implementation thoroughly.
    - Ensure all requirements are met before considering the task complete.
    - Fix any issues found during validation.

    ---

    Now, implement the PRP below:

    """


def load_prp_content(prp_path: Path) -> str:
    """Load and prepare PRP content for the AI model."""
    if not prp_path.exists():
        raise FileNotFoundError(f"PRP file not found: {prp_path}")
    
    prp_content = prp_path.read_text(encoding="utf-8")
    
    # Create the complete prompt
    prompt = META_HEADER + prp_content
    
    return prompt


def run_cursor_model(prompt: str, interactive: bool = False) -> None:
    """Run Cursor with the given prompt."""
    if interactive:
        # In interactive mode, we'll output the prompt and instructions
        print("=== PRP LOADED FOR CURSOR ===")
        print(prompt)
        print("\n=== INSTRUCTIONS ===")
        print("1. Copy the PRP content above")
        print("2. Paste it into Cursor")
        print("3. Follow the workflow guidance to implement the PRP")
        print("4. Use the validation commands to verify your implementation")
    else:
        # In headless mode, just output the prompt
        print(prompt)


def resolve_prp_path(prp_arg: str | None, prp_path_arg: str | None) -> Path:
    """Resolve PRP path from arguments."""
    if prp_path_arg:
        return Path(prp_path_arg)
    
    if prp_arg:
        return ROOT / f"{prp_arg}.md"
    
    raise ValueError("Must provide either --prp or --prp-path")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Run AI coding agent against a PRP (optimized for Cursor)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument(
        "--prp",
        help="Feature key; resolves to PRPs/{feature}.md"
    )
    
    parser.add_argument(
        "--prp-path",
        help="Path to a PRP markdown file (overrides --prp)"
    )
    
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive mode with instructions"
    )
    
    args = parser.parse_args()
    
    if not args.prp and not args.prp_path:
        parser.error("Must provide either --prp or --prp-path")
    
    try:
        prp_path = resolve_prp_path(args.prp, args.prp_path)
        prompt = load_prp_content(prp_path)
        run_cursor_model(prompt, args.interactive)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
