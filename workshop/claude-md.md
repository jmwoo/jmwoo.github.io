---
layout: workshop
title: "Module 3: CLAUDE.md"
page_number: 6
module: 3
---

# Module 3: CLAUDE.md / agents.md
**10:10 AM — Programming the Agent's Cognition (40 min)**

This is arguably the most important module. The CLAUDE.md file is the ONLY persistent context the agent gets every session. It's where you encode your project's DNA.

## 3.1 What CLAUDE.md Is

CLAUDE.md is a special file that Claude Code reads automatically at the start of every conversation. Think of it as a **project constitution**. Without it, Claude starts every session knowing nothing about your codebase, your conventions, or your preferences.

<div class="ws-callout ws-callout-key">
<strong>Key insight:</strong> LLMs can reliably follow about 150–200 instructions. Claude Code's own system prompt already uses about 50 of those. So your CLAUDE.md should be concise and focused — ideally under 300 lines, and shorter is better.
</div>

## 3.2 What Goes In It

| Section | Purpose | Example |
|---------|---------|---------|
| Project Overview | What this project does in 2–3 sentences | Express REST API for inventory management |
| Architecture | High-level design decisions | Monorepo, Postgres, Redis cache layer |
| Bash Commands | How to build, test, lint | `npm run test`, `npm run build` |
| Code Style | Language conventions and patterns | ES modules, functional components, Zod for validation |
| Constraints | Hard boundaries | Never modify `/migrations` directly |
| Non-Goals | What NOT to do | Don't add new dependencies without asking |
| Workflow | Step-by-step for the agent | Always run tests after changes |
