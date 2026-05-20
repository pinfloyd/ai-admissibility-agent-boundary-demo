# Paid Boundary Token Tier Candidate

Status: candidate only, not public-final.

Paid tier may enable selected external actions only if all are true:
1. valid access token
2. owner approval where required
3. external boundary returns ALLOW
4. local gate verifies action hash and scope
5. provider action matches approved recipient, subject, and body

No token means dry-run only. Token alone is not enough. Boundary ALLOW is still required.
