# Local Run

Created UTC: 2026-05-20T10:17:11.6053183Z

```bash
docker build -t ai-admissibility-agent .
docker run -v ./state:/app/state ai-admissibility-agent scan
```

Free mode is dry-run/read-only/local draft only. No Gmail, no outreach, no external action.
