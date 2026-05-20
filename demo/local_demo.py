import json, pathlib, datetime
root = pathlib.Path("/app")
required = ["README.md","LOCAL_RUN.md","CANDIDATE_STATUS.md","docs/SAFETY_AND_NO_SEND_PROOF.md","demo/SELF_SERVE_DEMO_FLOW.md"]
missing = [p for p in required if not (root / p).exists()]
status = {"schema":"ai-admissibility-public-safe-local-demo-v1","created_at":datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z","product":"AI Admissibility Agent + External Boundary/SAB","core_rule":"No Admission = No Execution","mode":"FREE_DRY_RUN_READ_ONLY_LOCAL_DEMO","required_found":len(required)-len(missing),"required_expected":len(required),"missing":missing,"email_sent":False,"outreach_done":False,"external_action_done":False,"execution_allowed_now":False,"local_self_allow":False,"github_changed":False,"site_changed":False,"server_changed":False,"cloudflare_changed":False}
print(json.dumps(status, indent=2, sort_keys=True))
raise SystemExit(0 if not missing else 2)
