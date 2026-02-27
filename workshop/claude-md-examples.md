---
layout: workshop
title: "Module 3: Good vs Bad CLAUDE.md"
page_number: 7
module: 3
---

# Good vs Bad CLAUDE.md

## 3.3 Side-by-Side Comparison

<div class="ws-two-col">
<div class="ws-col-bad">
<strong>Bad (vague, bloated)</strong><br><br>
"This is a web app. Please write good code. Use best practices. Make sure everything works. Be careful with the database."
</div>
<div class="ws-col-good">
<strong>Good (specific, concise)</strong><br><br>
"Express 5 + TypeScript API. Postgres via Prisma ORM. Run <code>npm test</code> after changes. Never modify <code>prisma/migrations/</code>. Use Zod for all input validation. Error responses follow RFC 7807."
</div>
</div>

<div class="ws-callout ws-callout-key">
<strong>Key principle:</strong> One concrete example is worth 100 words of explanation. Reference model files in your CLAUDE.md instead of describing patterns in prose.
</div>

## 3.4 Hands-On: Write a CLAUDE.md (15 min)

Have each attendee write a CLAUDE.md for the sample project (or their own project if they brought one). Walk around and review.

**Common mistakes to correct:**
- Too long / too much irrelevant detail
- Too vague ("write clean code")
- Missing the bash commands (build, test, lint)
- Missing constraints (what NOT to do)

<div class="ws-callout ws-callout-tip">
<strong>Pro Tip: Nested CLAUDE.md Files</strong><br><br>
You can place CLAUDE.md files in subdirectories for more specific context:
<ul>
<li>Root <code>CLAUDE.md</code>: universal project rules</li>
<li><code>/frontend/CLAUDE.md</code>: React-specific patterns</li>
<li><code>/tests/CLAUDE.md</code>: testing conventions</li>
</ul>
This keeps each file focused and concise.
</div>
