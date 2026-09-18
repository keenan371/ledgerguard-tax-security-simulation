# LedgerGuard Portfolio Walkthrough Runbook

## Recording goal

Show an evidence-to-risk-to-remediation-to-verification workflow for a fictional seven-person accounting firm. The recording is proof of Keenan's process and judgment, not a claim of paid client work or a live Microsoft 365 deployment.

Target length: **6-8 minutes**.

## Do not record yet

Complete this preflight first:

- Close email, Notion, terminals and browser tabs containing real prospect or account data.
- Open the repository README and the files listed below in presentation order.
- Open `portfolio/portfolio_gallery.html` in a browser.
- Set browser/editor zoom so headings and tables are readable at 1080p.
- Confirm the repository banner says the environment and evidence are fictional/synthetic.
- Disable desktop notifications.
- Perform one silent rehearsal and verify the microphone.

## Hit Record

Hit **Record** only after the gallery is open on `01_training_overview.png`, the cursor is parked away from the content and the fictional-simulation disclosure is visible.

## Scene-by-scene walkthrough

### 1. Context and disclosure - 30 seconds

Show: `README.md` and `portfolio/01_training_overview.png`.

Say:

> This is LedgerGuard, a fictional tax-firm security simulation I built to demonstrate how I scope, assess, prioritize, improve and verify security controls. It uses synthetic evidence only. No real client, tenant or taxpayer data appears anywhere in the project.

### 2. Scope and rules of engagement - 45 seconds

Show: `01_SCOPE_AND_RULES_OF_ENGAGEMENT.md` and `portfolio/06_scope_guardrails.png`.

Explain the authorized systems, exclusions, client responsibilities and stop conditions. Emphasize that controlled scope is part of security engineering.

### 3. Evidence and architecture - 60 seconds

Show: `00_SCENARIO/DATA_FLOW.md`, `02_SIMULATED_EVIDENCE_REGISTER.csv` and `portfolio/02_evidence_register.png`.

Explain how evidence receives an ID, source, owner and verification status. Point out the identity, endpoints, backup, logging, vendors and incident-response data flows.

### 4. IAM findings - 75 seconds

Show: `03_RISK_ASSESSMENT/GAP_REGISTER.md`, the identity findings in `data/risk_register.csv`, and `08_PORTFOLIO/screenshots/05_mfa.png`.

Explain:

- Account inventory and role mapping
- MFA coverage
- Least privilege and administrative separation
- Joiner/mover/leaver controls
- Evidence required before an access finding can be marked resolved

### 5. Risk prioritization - 60 seconds

Show: `03_RISK_ASSESSMENT.md` and `portfolio/03_risk_prioritization.png`.

Explain likelihood, impact, priority and business context. Demonstrate why a smaller number of verified high-priority fixes is more useful than an unfiltered scanner dump.

### 6. Remediation and verification - 90 seconds

Show: `04_REMEDIATION_ROADMAP.md`, `05_VERIFICATION_PLAN_AND_RESULTS.md` and `portfolio/05_verification_matrix.png`.

For one IAM control and one backup or logging control, trace:

```text
Evidence -> finding -> owner -> remediation -> acceptance test -> result -> residual risk
```

State clearly that implementation results are simulated and the value demonstrated is the repeatable verification method.

### 7. Client handoff - 60 seconds

Show: `06_FINAL_CLIENT_PACKAGE.md`, `07_CLIENT_DELIVERABLES/EXECUTIVE_SUMMARY.md` and `portfolio/04_first_30_days.png`.

Explain how technical findings become an owner-readable plan with named responsibilities, timing, evidence and decisions.

### 8. Close - 30 seconds

Show: GitHub repository homepage.

Say:

> This project demonstrates the way I approach IAM, endpoint, backup, logging and incident-readiness work: define the boundary, collect evidence, prioritize risk, make bounded changes and verify the result. If your organization or MSP needs this kind of structured security work, contact BlueHippoCyber.

## Required captures

Export or retain clean frames for:

1. Scenario overview
2. Scope guardrails
3. Evidence register
4. IAM/MFA gap
5. Risk register
6. Remediation roadmap
7. Verification matrix
8. Executive summary

## Claim guardrails

Never call LedgerGuard a customer, testimonial, production tenant or completed paid engagement. Do not claim FTC compliance, certification, guaranteed breach prevention or live remediation. Use “fictional simulation,” “synthetic evidence,” “designed,” “modeled” and “demonstrates.”

