# Historical design note — Payment Token Mechanism Spec

**Status: historical reference only. Not an active payment, access, or credential mechanism.**

This file records an earlier design exploration involving Stripe or Lemon Squeezy and access-token issuance.

That mechanism is not part of the current public product surface.

The current website and GitHub repositories do not:

- process checkout;
- issue access tokens or credentials;
- unlock paid execution modes;
- run customer production workloads.

Current public status:

https://ai-admissibility.com/

The only architectural rule carried forward from this design is that commercial or identity context, if used in a future deployment, must never replace the external admission decision itself.

**No Admission = No Execution.**
