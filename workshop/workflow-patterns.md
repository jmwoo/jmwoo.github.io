---
layout: workshop
title: "Module 4: Plan-Execute-Review"
page_number: 8
module: 4
---

# Module 4: Workflow Patterns & Control
**10:50 AM — Skills That Separate Amateurs from Power Users (40 min)**

## 4.1 The Plan-Execute-Review Loop

This is the **single most important workflow pattern**. Never let the agent just start coding on a complex task.

1. **Ask for a plan:** "Create an implementation plan for X. Do not write any code yet."
2. **Review the plan:** Question assumptions. Correct direction. Add constraints.
3. **Execute in steps:** "Implement step 1 of your plan." Then review. Then step 2.
4. **Verify:** "Run the tests. Show me the diff."

<div class="ws-callout ws-callout-tip">
<strong>Live Demo:</strong> Show this loop live with a real feature. Deliberately DON'T plan first — let it go off the rails. Then restart with the plan-first approach. The contrast is powerful.
</div>

## 4.2 Task Decomposition

Teach them to break features into atomic operations. The biggest beginner mistake is "Build me X."

<div class="ws-two-col">
<div class="ws-col-bad">
<strong>Too broad</strong><br><br>
"Build a user authentication system."
</div>
<div class="ws-col-good">
<strong>Right granularity</strong><br><br>
"Step 1: Create the User model with email and hashed password fields.<br>
Step 2: Write the registration endpoint with Zod validation.<br>
Step 3: Write unit tests for registration."
</div>
</div>

## 4.3 Control Patterns (The Power Moves)

These phrases change the agent's behavior dramatically:

| Say This | Effect |
|----------|--------|
| "Do not write code yet." | Forces planning mode |
| "Ask me 3 clarifying questions before proceeding." | Surfaces assumptions |
| "List your assumptions." | Makes hidden reasoning visible |
| "Explain your plan before implementing." | Catches misunderstandings early |
| "Think hard about this." | Engages extended reasoning (more compute) |
| "Search the codebase for X before editing." | Prevents hallucination about existing code |
