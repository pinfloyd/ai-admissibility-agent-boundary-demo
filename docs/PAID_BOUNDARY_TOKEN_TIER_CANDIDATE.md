# Historical design note — Paid Boundary Token Tier Candidate

**Status: historical reference only. Not the current public product route.**

This file is retained to document an earlier design exploration.

The current public AI Admissibility surface does not process payments, issue access tokens, or provide customer production execution through the website or these GitHub repositories.

Current status and canonical public demonstration:

https://ai-admissibility.com/

## Earlier candidate concept

The earlier candidate proposed that a paid tier might enable selected external actions only if all were true:

1. valid access token;
2. owner approval where required;
3. external boundary returns ALLOW;
4. local gate verifies action hash and scope;
5. provider action matches approved recipient, subject, and body.

The architectural point that remains valid is that a token alone must never substitute for external admission.

**No Admission = No Execution.**
