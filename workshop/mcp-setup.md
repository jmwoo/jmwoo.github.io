---
layout: workshop
title: "Module 5: Setting Up MCP"
page_number: 12
module: 5
---

# Setting Up MCP Servers

## 5.3 Configuration

Walk through adding an MCP server to Claude Code. Keep it simple for the workshop — filesystem and GitHub are the most universally useful.

The configuration lives in `~/.claude/settings.json` or the project's `.mcp.json`. Show them how to add a server and verify it's connected.

<div class="ws-callout ws-callout-tip">
Don't go deep into building custom MCP servers — that's an advanced topic for another day. Focus on connecting and using existing servers.
</div>

<div class="ws-callout ws-callout-warn">
<strong>Context Budget Warning</strong><br><br>
Share this insight from power users: "If your MCP servers are using more than 20k tokens of context, you're crippling Claude. That leaves very little room for actual work."<br><br>
Be selective about which MCP servers you enable. More is not always better.
</div>
