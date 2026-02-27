---
layout: workshop-deck
title: "Get Started"
page_number: 3
deck: agentic-coding-live
deck_title: "Agentic Coding"
permalink: /agentic-coding/get-started/
---

# Get Started

- initialize the agent, define rules, and keep the repo clean.

- run `/init` if supported.

- `CLAUDE.md` or `AGENTS.md`
	- file the agent reads automatically at the start of every "session"
	- conventions, preferences, etc..
	- less is more

## `AGENTS.md` template

```md
# Project Overview
[What this project does in 2-3 sentences]

# Architecture
[High-level design: tech stack, key directories, data flow]

# Bash Commands
- Build: [command]
- Test: [command]
- Lint: [command]

# Code Style
[Language, patterns, conventions, formatting]

# Constraints
- NEVER [hard boundaries]
- ALWAYS [required patterns]

# Workflow
1. Plan before coding
2. Start features in new branch
3. Implement in small steps
4. Run tests after changes
5. Commit with descriptive messages
```
