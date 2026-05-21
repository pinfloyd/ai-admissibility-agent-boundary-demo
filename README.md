# AI Admissibility Agent + External Boundary

AI Admissibility is packaged as Agent + External Boundary/SAB.

The agent prepares sales intelligence, local briefs, and draft-only text. External actions remain gated by admission.

## Core rule

No Admission = No Execution.

## Demo promise

The demo shows useful preparation, not uncontrolled autonomy. The agent reads public signals, creates local briefs, and prepares draft-only text.

## What this is not

- Not a scanner.
- Not monitoring.
- Not rollback.
- Not a generic guardrail.
- Not a certification or universal safety claim.

## Local run concept

docker run -v ./state:/app/state ai-admissibility-agent scan

## Free vs paid candidate

Free: dry-run, read-only, local draft only. Paid candidate: external actions require token plus boundary ALLOW. Pricing is candidate-only, not final public pricing.

---

## What this demo proves

This public demo shows an agent workflow bound to an external admission boundary. The agent may prepare local intent, local evidence, and public-safe candidate material, but external execution is not allowed unless the hosted authority returns a signed ALLOW for the exact request.

Core rule: No Admission = No Execution.

## What this demo does not claim

This repository is not the full commercial product, not private enforcement logic, not payment infrastructure, not a customer deployment, and not a general safety guarantee.

## Boundary decision model

Agent prepares intent -> external boundary evaluates the exact request -> ALLOW permits the next controlled step -> DENY or FAIL blocks execution.

## Hash contract

For HOSTED_L5_AUTHORITY_V2 with ai-secrets-v1, added_lines_sha256 is SHA256 over added_lines joined by newline with no trailing final newline.
