---
layout: workshop
title: "Module 5: MCP Overview"
page_number: 11
module: 5
---

# Module 5: MCP (Model Context Protocol)
**11:45 AM — Giving the Agent Hands (30 min)**

This module differentiates users who get decent results from those who get incredible results. MCP is what turns the agent from a text generator into an autonomous contributor.

## 5.1 What MCP Is (Conceptual)

Use the "USB-C for AI" analogy: just as USB-C provides a standardized way to connect devices, MCP provides a standardized way to connect AI agents to external tools and data sources. Before MCP, every integration was custom. MCP makes it plug-and-play.

MCP was introduced by Anthropic in November 2024 and has since been adopted by OpenAI, Google DeepMind, and major toolmakers. It was donated to the Linux Foundation in December 2025, making it a true open standard.

**The three MCP primitives:**

| Primitive | What It Does | Controlled By |
|-----------|-------------|---------------|
| **Tools** | Actions the model can take (run a query, create a file, send a message) | Model |
| **Resources** | Data sources the model can read (files, database schemas, API docs) | App |
| **Prompts** | Pre-crafted instruction templates for common workflows | User |

## 5.2 Practical MCP Examples

Show the impact with concrete patterns:

- "Search the codebase before editing" → Filesystem MCP
- "Run tests after every change" → Shell/Bash tools
- "Check the database schema before writing a query" → Database MCP
- "Fetch the current GitHub issues" → GitHub MCP
- "Get up-to-date library documentation" → Context7 or Docs MCP (prevents hallucination on new APIs)

<div class="ws-callout ws-callout-tip">
<strong>Live Demo: MCP in Action (10 min)</strong><br><br>
Show a before/after. Without MCP: agent hallucinates API syntax. With documentation MCP: agent reads the actual docs and gets it right. This is a "mind-blown" moment for most people.
</div>
