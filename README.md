# LedgerGuard Tax & Accounting LLC — Security Practice Simulation

**FICTIONAL TRAINING SIMULATION — NO REAL TENANT, CLIENT, TAXPAYER, OR SYSTEM WAS ACCESSED.**

A fully local, fictional security-engineering and consulting-delivery lab for a seven-person Central Florida independent accounting firm. It models how an assessor moves from discovery and evidence collection through identity and access review, risk prioritization, remediation planning, verification, and client handoff. It deliberately contains no credentials, taxpayer records, tenant identifiers, live URLs, production commands, or external integrations.

## Why this is a cybersecurity / IT / IAM lab

The accounting-firm scenario is the business context—not the limit of the technical skills demonstrated. The same workflow applies to MSP clients, internal IT teams, and small-to-mid-sized organizations that need defensible security improvements.

- **Identity and access management:** account inventory, role mapping, least privilege, MFA coverage, privileged-access review, joiner/mover/leaver thinking, and evidence-based access verification.
- **Security engineering:** translating risks into bounded control changes and defining pass/fail verification instead of treating remediation as complete when a setting is merely changed.
- **IT operations:** endpoint, backup, logging, remote-access, vendor-access, and incident-readiness dependencies.
- **Risk and assurance:** traceable findings, risk scoring, evidence registers, remediation ownership, residual risk, and executive-ready reporting.
- **Client delivery:** scope control, rules of engagement, implementation boundaries, acceptance criteria, time/cost tracking, and final handoff.

## Delivery flow

```text
Discovery and scope
        ↓
Synthetic evidence register
        ↓
IAM + endpoint + backup + logging gap analysis
        ↓
Risk-ranked remediation roadmap
        ↓
Control verification and residual-risk review
        ↓
Client package + portfolio-safe proof
```

## Scenario model
- Firm: LedgerGuard Tax & Accounting LLC (fictional)
- Team: owner/CPA, office manager, three tax preparers, bookkeeper, seasonal assistant
- Modeled stack: Microsoft 365 Business, Windows endpoints + owner laptop, generic tax application, shared storage/email/remote access/backups/vendor relationships
- Assessment basis: interview-style assumptions and simulated control evidence dated 2026-09-17

## Package map
- `01_SCOPE_AND_RULES_OF_ENGAGEMENT.md` — boundaries and exclusions
- `02_SIMULATED_EVIDENCE_REGISTER.csv` — 14 sanitized evidence items
- `03_RISK_ASSESSMENT.md` + `data/risk_register.csv` — scored risk register and method
- `04_REMEDIATION_ROADMAP.md` — prioritized, finite action plan
- `05_VERIFICATION_PLAN_AND_RESULTS.md` — repeatable verification with simulated results
- `06_FINAL_CLIENT_PACKAGE.md` — client-facing handoff draft
- `07_TIME_AND_COST_TRACKER.csv` — internal estimate/actual tracker
- `08_MVC_DELIVERY_PLAYBOOK.md` — minimum viable consulting delivery workflow
- `09_MVC_ASSETS.md` — discovery, intake, offer and QA assets
- `10_COMPLETION_REPORT.md` — truthful cold-call readiness gate
- `portfolio/` — 8 sanitized portfolio images and capture manifest

## Safety and claim boundary
This package demonstrates documentation, prioritization, and verification design only. It does **not** demonstrate a Microsoft 365 review, endpoint inspection, penetration test, incident response, legal determination, certification, or managed monitoring. Do not present it as proof of completed client work.

## Portfolio proof

The repository includes the scenario, scope, synthetic evidence, scored findings, remediation roadmap, verification plan/results, client-facing package, delivery playbook, time/cost model, and eight sanitized presentation images. Together, they show the reasoning trail from a business problem to security controls and measurable acceptance criteria. A recorded walkthrough should preserve the same fictional/synthetic disclosure.

**Human/legal review draft:** This material is operational training content, not legal, tax, compliance, certification, or insurance advice.
