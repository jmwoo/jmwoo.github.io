---
layout: workshop
title: "Module 2: Getting Started"
page_number: 5
module: 2
---

# Module 2: Getting Started
**9:30 AM — Environment Setup & First Steps (40 min)**

## 2.1 The Tool Landscape

Briefly orient them on what's available and why you're focusing on Claude Code:

- **Claude.ai (web):** Great for quick tasks, artifacts, non-devs. No terminal needed.
- **Claude Code (CLI):** The power tool. Works in your terminal, reads your codebase, runs commands, manages files. This is our primary focus.
- **Cursor / Windsurf / Copilot:** IDE-integrated options. Same principles apply — context management is the skill, not the specific tool.

## 2.2 First Run with Claude Code

Walk them through:

1. Open a terminal in a sample project directory
2. Run: `claude` (this starts the interactive session)
3. Run: `/init` (this generates a starter CLAUDE.md by analyzing the project)
4. Review the generated CLAUDE.md together as a group

## 2.3 Repo Hygiene Matters

Emphasize this strongly: the agent's output quality is directly proportional to the quality of your project's organization. A messy repo produces messy results.

- **Clean folder structure:** The agent reads your filesystem. If it's chaos, it'll be confused.
- **Working build/tests:** If the agent can't run your tests, it can't verify its own work.
- **Good Git hygiene:** Always work on a branch. Commit before and after agent sessions. This is your undo button.

<div class="ws-callout ws-callout-quote">
"Garbage repo = garbage agent output." The #1 takeaway from experienced Claude Code users: 500 words of good project context can transform 500MB of broken code into 30KB of working code.
</div>
