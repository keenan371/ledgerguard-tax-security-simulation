# 05 — Verification Plan and Simulated Results

**FICTIONAL TRAINING SIMULATION — NO REAL TENANT, CLIENT, TAXPAYER, OR SYSTEM WAS ACCESSED.**

## Verification protocol
Verification is evidence-based, least-invasive, and performed only after a real client approves a change. Never collect taxpayer files or passwords. Record only minimum metadata needed to demonstrate completion.

| Control | Evidence requested | Pass rule | Simulated training result | Status |
|---|---|---|---|---|
| MFA | User roster with enrollment state | All six named staff are enrolled; exceptions documented | 4/6 enrolled in baseline; remediation not executed | Not passed — simulated baseline |
| Admin separation | Role worksheet + procedure | Daily account has no standing admin role or approved exception | No separate admin workflow evidenced | Not passed — simulated baseline |
| Encryption | Device compliance export | 8/8 devices verified encrypted or approved exception | 6 verified / 2 unknown | Not passed — simulated baseline |
| Updates | Compliance summary | Supported devices updated within approved cadence | 3 devices >30 days behind | Not passed — simulated baseline |
| Endpoint protection | Protection-status export | 8/8 active or approved exception | 7 active / 1 unverified | Not passed — simulated baseline |
| Restore | Dated restore-test record | Test completes with documented result and follow-up | No record available | Not passed — simulated baseline |
| Access review | Matrix + sign-off | Role access approved and exceptions time-bound | Broad access pending review | Not passed — simulated baseline |
| Incident readiness | Escalation card/tabletop acknowledgment | Named contacts and first actions confirmed | No card evidenced | Not passed — simulated baseline |

## Verification safeguards
- Use a client-provided privileged operator for any real admin console action.
- Redact user identifiers, serial numbers, email addresses, ticket numbers, and client data from shared evidence.
- Retain only approved evidence under the client’s retention policy.
- A "pass" validates one criterion at one point in time; it is not certification or a security guarantee.

**Human/legal review draft:** This material is operational training content, not legal, tax, compliance, certification, or insurance advice.
