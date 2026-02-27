---
layout: workshop
title: "Appendix: Quick Reference"
page_number: 17
---

# Appendix: Quick Reference Materials

## A: Prompt Control Cheat Sheet

| Say This | To Get This |
|----------|-------------|
| "Do not write code yet." | Forces planning mode |
| "Ask me 3 clarifying questions." | Surfaces hidden assumptions |
| "List your assumptions." | Makes reasoning explicit |
| "Think hard about this." | Engages extended reasoning |
| "Search the codebase first." | Prevents hallucination |
| "Explain your plan before implementing." | Catches misunderstandings |
| "Implement step 1 only." | Keeps scope tight |
| "Review this for security issues." | Agent self-critiques |
| "Run the tests." | Verifies its own work |
| "Use a subagent to investigate X." | Preserves main context |

## B: CLAUDE.md Template

```markdown
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
2. Implement in small steps
3. Run tests after changes
4. Commit with descriptive messages
```

## C: Workflow Checklist

- [ ] Start a new branch before any agent work
- [ ] Write / update CLAUDE.md with project context
- [ ] Define the task in 2–3 clear sentences
- [ ] Ask the agent to plan (not code) first
- [ ] Review the plan and correct assumptions
- [ ] Implement one step at a time
- [ ] Run tests after each step
- [ ] Review diffs before accepting
- [ ] Commit after each successful step
- [ ] Use `/compact` or `/clear` when context gets long

## D: If You Only Have 2 Hours

Cut Modules 5 (deep MCP) and 7 (advanced failure modes). Keep:

| Time | Module | Topic |
|------|--------|-------|
| 20 min | 1 | Mindset shift + wow demo |
| 30 min | 3 | CLAUDE.md — the highest-ROI skill |
| 20 min | 4 | Plan-execute-review + control patterns |
| 40 min | 6 | Hands-on build session |
| 10 min | 8 | Quick wrap-up with resources |
