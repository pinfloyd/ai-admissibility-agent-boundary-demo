# AI Admissibility Agent + External Boundary Demo

This repository is a bounded demonstration surface for an agent workflow constrained by an external admission boundary.

Official product surface:

https://ai-admissibility.com/

**No Admission = No Execution.**

## What this demo shows

The agent may prepare local intent, evidence, and draft-only material. Protected external execution requires an admission decision for the exact request.

Agent prepares intent -> external boundary evaluates -> ALLOW permits the next controlled step -> DENY or failure blocks execution.

## What this repository is not

- not the canonical installed runtime;
- not the public Marketplace Action;
- not payment infrastructure;
- not a customer deployment;
- not a universal safety or compliance guarantee.

## Historical note

Some demonstration material in this repository refers to earlier hosted-authority identifiers such as `HOSTED_L5_AUTHORITY_V2`. Those identifiers describe historical proof artifacts and must not be interpreted as the current canonical runtime identity.

For current product status and terminology, use:

https://ai-admissibility.com/

## Related surfaces

- Boundary architecture / proof: https://github.com/pinfloyd/ai-admissibility-boundary
- Current Marketplace evaluation Action: https://github.com/pinfloyd/ai-admissibility-action
- Request access: https://ai-admissibility.com/request
