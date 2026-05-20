# Payment Token Mechanism Spec

Candidate providers: Stripe or Lemon Squeezy.

Flow:
1. Payment succeeds.
2. System issues an access token.
3. Token is stored in .env for local runtime.
4. Runtime checks token before paid mode.
5. External action still requires boundary ALLOW.

Free mode: no token means WOULD_SEND only; no email is sent.
