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
