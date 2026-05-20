# Docker Package Plan

Goal: make the Agent + Boundary dry-run package easy to try locally.

Requirements:
- State volume: /app/state
- No secrets required for free dry-run
- No Gmail, SMTP, or provider send in demo mode
- Boundary token only for future paid external action mode

Candidate command:
docker run -v ./state:/app/state ai-admissibility-agent scan
