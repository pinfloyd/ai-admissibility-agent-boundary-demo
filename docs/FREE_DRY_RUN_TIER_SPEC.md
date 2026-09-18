# Historical design note — Free Dry-Run Tier Spec

**Status: historical reference for the bounded local demo. Not a current tier or pricing surface.**

The earlier demo model used a local-only dry-run mode.

Its safety properties remain useful as a demonstration pattern:

Allowed:

- public signal discovery;
- local scoring;
- local brief generation;
- draft-only text generation.

Forbidden:

- Gmail draft creation;
- email send;
- outreach;
- external action;
- production execution.

Hard demo status:

- EMAIL_SENT=NO
- OUTREACH_DONE=NO
- EXTERNAL_ACTION_DONE=NO

The current public product does not expose free/paid tiers through the website. Current status is maintained at:

https://ai-admissibility.com/
