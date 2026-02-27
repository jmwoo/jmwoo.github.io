---
layout: workshop
title: "Module 4: Context Management"
page_number: 9
module: 4
---

# Context Management

## 4.4 Progressive Refinement Pattern

For any substantial piece of work, teach this cycle:

1. **Spec** — Get the requirements right
2. **Draft** — First pass implementation
3. **Critique** — "Review this code for edge cases, security issues, and performance."
4. **Refactor** — Apply the critique
5. **Harden** — Add tests, error handling, logging

<div class="ws-callout ws-callout-key">
The agent is exceptionally strong at iteration loops. Use this to your advantage.
</div>

## 4.5 Context Management

This is the #1 technical constraint. Claude Code's context window fills up fast, and performance degrades as it fills.

**Key practices:**

- **One feature per chat session.** Don't try to do everything in one conversation.
- **Use `/compact`** when running low on context (it summarizes the conversation)
- **Use `/clear`** to start fresh when switching tasks
- **Scope investigations narrowly:** "Search only in `/src/auth` for..." not "Search the whole codebase"
- **Use sub-agents for research:** "Use a subagent to investigate how our auth middleware works."

<div class="ws-callout ws-callout-warn">
<strong>Watch out:</strong> Long conversations where the agent loses track of earlier decisions are one of the most common failure modes. When you notice the agent repeating mistakes or contradicting itself, it's time for <code>/compact</code> or <code>/clear</code>.
</div>
