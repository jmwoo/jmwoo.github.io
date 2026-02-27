---
layout: workshop-deck
title: "MCP"
page_number: 6
deck: agentic-coding-live
deck_title: "Agentic Coding"
permalink: /agentic-coding/mcp/
---

# MCP

- let your agent use other people's developed tools

- examples:
	- context7
	- playwright

- My favorite: postgres MCP
	- demo?

- Capabilities: files, APIs, databases, dev/cloud systems.
- Impact: turns chat into an operational workflow.
- Safety: least privilege, explicit approvals, human review.

## Example MCPs (easy -> advanced)

1. Filesystem MCP: read/write project files and generate code changes.
2. GitHub MCP: open issues, inspect PRs, and post review comments.
3. Production Ops MCP: query telemetry, run safe diagnostics, and trigger controlled deploy workflows.

## Install MCP (Codex + Claude Code)

- Codex: Settings -> MCP Servers -> Add Server -> provide server command/env -> connect -> verify tools appear.
- Claude Code: configure MCP in `~/.claude/settings.json` or project `.mcp.json`, then restart session and verify tool list.
