---
layout: workshop
title: "Module 7: Failure Modes"
page_number: 15
module: 7
---

# Module 7: Failure Modes & Guardrails
**1:15 PM — The Honest Talk (20 min)**

Engineers need realism. Don't oversell. This section builds trust and credibility.

## 7.1 Common Failure Modes

- **Over-delegation:** Asking the agent to build too much at once. It loses coherence. Keep scope small.
- **Hidden hallucinations:** Code that looks right but uses APIs that don't exist, or logic that subtly breaks. Always verify.
- **Silent incorrect assumptions:** The agent makes decisions about architecture, dependencies, or patterns without telling you. Use "list your assumptions" liberally.
- **Context drift:** Long conversations where the agent loses track of earlier decisions. Use `/compact` or start fresh.
- **The infinite loop:** Agent tries the same failing fix 3+ times. Recognize this. Break the cycle with `/clear`, revert the changes, and restate the problem differently.
- **Security leaks:** Agent may hardcode secrets, skip input validation, or use insecure patterns. Always review security-critical code manually.

## 7.2 Safety Patterns

- Always work on a branch. "Commit early, vibe often."
- Require the agent to explain its reasoning before you accept changes
- Require test generation for any new feature
- Review diffs before committing (learn to read diffs quickly)
- Keep scope small per session. One feature, one conversation.
- Use Git as your safety net. You can always revert.

## 7.3 When NOT to Vibe Code

<div class="ws-callout ws-callout-warn">
Be honest about limitations:
<ul>
<li><strong>Security-critical authentication/encryption logic</strong> → Write and review manually</li>
<li><strong>Complex distributed systems architecture</strong> → The agent lacks your domain knowledge</li>
<li><strong>Regulatory compliance code</strong> → Requires human accountability</li>
<li><strong>Performance-critical hot paths</strong> → Agent may not optimize for your specific constraints</li>
</ul>
</div>
