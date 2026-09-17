from pathlib import Path
from datetime import date
import json

ROOT = Path(r"C:\Users\ronin\OneDrive\Desktop\BLUEHIPPOCYBER_AIOS\09_DIGITAL PRODUCTS\01_SecurityPracticeOS\labs\LedgerGuard_Tax_Security_Simulation")
SALES = Path(r"C:\Users\ronin\OneDrive\Desktop\BLUEHIPPOCYBER_AIOS\09_DIGITAL PRODUCTS\01_SecurityPracticeOS\sales\hermes-background\2026-09-17")

notice = "**FICTIONAL TRAINING SIMULATION — NO REAL TENANT, CLIENT, TAXPAYER, OR SYSTEM WAS ACCESSED.**"
legal = "**Human/legal review draft:** This material is operational training content, not legal, tax, compliance, certification, or insurance advice."

def write(rel, body, sales=False):
    path = (SALES if sales else ROOT) / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")

write("README.md", f"""# LedgerGuard Tax & Accounting LLC — Security Practice Simulation

{notice}

A fully local, fictional delivery/MVC package for a seven-person Central Florida independent accounting firm. It models a fixed-scope security readiness engagement and deliberately contains no credentials, taxpayer records, tenant identifiers, live URLs, production commands, or external integrations.

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

{legal}
""")

write("01_SCOPE_AND_RULES_OF_ENGAGEMENT.md", f"""# 01 — Scope and Rules of Engagement

{notice}

## Engagement objective
Create a limited security-readiness baseline and a practical 30/60/90-day improvement roadmap for the fictional LedgerGuard Tax & Accounting LLC. The modeled outcome is better protection of sensitive tax-workflow information through identity, endpoint, backup, vendor, and staff-process controls.

## In scope (training model)
| Workstream | Modeled activity | Output |
|---|---|---|
| Discovery | 90-minute owner/office-manager interview and inventory worksheet | Asset/control assumptions |
| Identity | Review MFA, admin role, shared-account, and password-policy evidence excerpts | Identity findings |
| Endpoint | Review simulated device inventory, update status, encryption and protection status | Endpoint findings |
| Data resilience | Review backup questionnaire, restore-test record, and shared-storage access model | Recovery findings |
| Workflow | Review remote-access, vendor, phishing, and incident-escalation process statements | Process findings |
| Closeout | Prioritized register, roadmap, owner handoff, verification checklist | Draft client package |

## Explicit exclusions
- Legal, tax, privacy, breach-notification, or regulatory advice; all policy language requires human/legal review.
- Any certification, guarantee, audit opinion, attestation, or compliance determination.
- Penetration testing, vulnerability exploitation, phishing simulation, forensics, or incident response.
- Major tenant migration, identity redesign, software implementation, hardware procurement, or unlimited remediation.
- 24/7 monitoring, managed IT, ongoing SOC/NOC activity, or emergency support.
- Hardware, software, license, travel, tax, or third-party vendor costs; those are separate customer decisions.
- Access to any real tenant, email, endpoint, backup, tax application, customer record, or taxpayer data.

## Authorization boundary
All evidence is invented and sanitized. The exercise author may only edit files inside this simulation folder and the designated internal sales folder. No FamilyConnect material or Hermes profile is in scope.

## Decision gates
1. Before any real engagement: executed agreement, authorized contact, approved scope, and data-handling plan.
2. Before configuration changes: client approval, backup/rollback plan, named change owner, and maintenance window.
3. Before policy/legal statements: qualified human/legal review.
4. Before service expansion: separately scoped statement of work and commercial approval.

{legal}
""")

write("02_SIMULATED_EVIDENCE_REGISTER.csv", """evidence_id,domain,artifact,simulated_observation,classification,source_type,review_status,retention_note
E-001,Identity,MFA status export excerpt,6 named users modeled; 4 MFA-enrolled; 2 pending,Confidential-training,Mock CSV,Reviewed,No live directory data
E-002,Identity,Admin role worksheet,Owner account modeled as daily-use administrator,Confidential-training,Interview note,Reviewed,No actual account name
E-003,Identity,Shared mailbox worksheet,2 shared inboxes modeled with unclear delegated access review,Confidential-training,Interview note,Reviewed,No mail content
E-004,Endpoint,Device inventory,8 Windows devices modeled; 6 encrypted; 2 status unknown,Confidential-training,Mock inventory,Reviewed,No serials or users
E-005,Endpoint,Update status summary,3 devices modeled more than 30 days behind updates,Confidential-training,Mock dashboard excerpt,Reviewed,No endpoint telemetry
E-006,Endpoint,Protection status summary,7 of 8 devices modeled with active endpoint protection; 1 unverified,Confidential-training,Mock dashboard excerpt,Reviewed,No product telemetry
E-007,Data,Backup questionnaire,Cloud backup assumed but restore test not documented in prior 12 months,Confidential-training,Questionnaire,Reviewed,No backup configuration
E-008,Data,Shared storage access map,Tax workspace modeled with broad group access pending role review,Confidential-training,Mock access matrix,Reviewed,No document names
E-009,Remote access,Remote access statement,Owner laptop remote access method not standardized or documented,Confidential-training,Interview note,Reviewed,No remote endpoint
E-010,Awareness,Training roster,Annual phishing-awareness training not evidenced for all modeled roles,Confidential-training,Mock roster,Reviewed,No staff identities
E-011,Vendor,Vendor register,Tax software support and cloud storage vendor contacts not centralized,Confidential-training,Mock register,Reviewed,No vendor contracts
E-012,Incident,Escalation card,No one-page incident escalation card evidenced,Confidential-training,Mock policy review,Reviewed,No incident data
E-013,Governance,Policy index,Acceptable-use and access-review cadence marked draft/not approved,Confidential-training,Mock index,Reviewed,No policy provenance
E-014,Resilience,Restore test record,No dated restore validation evidence available in scenario,Confidential-training,Mock record review,Reviewed,No real backups
""")

write("data/risk_register.csv", """risk_id,domain,risk_statement,likelihood,impact,inherent_score,existing_control,residual_score,priority,owner,target_window,verification_evidence
R-01,Identity,Two modeled users lack MFA enrollment,4,5,20,Partial enrollment,16,Critical,Owner/Office Manager,0-14 days,MFA roster shows 6 of 6 named users enrolled
R-02,Identity,Daily-use owner account retains administrator role,4,5,20,No separate admin account evidenced,15,High,Owner,0-30 days,Role worksheet and separate admin procedure
R-03,Endpoint,Two modeled devices have unknown encryption status,3,5,15,Inventory exists but incomplete,12,High,Office Manager,0-30 days,Device report confirms encryption or documented exception
R-04,Endpoint,Three modeled devices are over 30 days behind updates,4,4,16,Ad hoc updates,12,High,Office Manager,0-30 days,Update compliance report shows supported patch level
R-05,Resilience,Restore testing is not documented,3,5,15,Backup assumed present,12,High,Owner/Bookkeeper,0-30 days,Dated successful restore test record
R-06,Data,Shared tax workspace access may be broader than job need,3,5,15,Group access used,10,High,Owner/Office Manager,15-45 days,Approved role/access matrix and access review sign-off
R-07,Endpoint,One modeled device endpoint protection status is unverified,3,4,12,Protection on most devices,8,Medium,Office Manager,15-45 days,Protection console/export or documented exception
R-08,Awareness,Training completion is not evidenced for all roles,3,4,12,Informal reminders,8,Medium,Office Manager,15-60 days,Completion roster and annual cadence
R-09,Remote access,Remote owner-laptop access is not standardized,3,4,12,Informal process,8,Medium,Owner,15-60 days,Approved remote access standard and inventory
R-10,Vendor,Vendor contacts and escalation terms are decentralized,2,4,8,Individual emails,6,Medium,Office Manager,30-60 days,Vendor register with owner/support/escalation fields
R-11,Incident,No concise incident escalation card is evidenced,3,4,12,Verbal escalation,8,Medium,Owner,0-30 days,Approved call tree/tabletop acknowledgment
R-12,Governance,Access review and acceptable-use policies remain draft,2,4,8,Draft language only,6,Medium,Owner,30-90 days,Human/legal reviewed policy approval record
""")

write("03_RISK_ASSESSMENT.md", f"""# 03 — Risk Assessment

{notice}

## Method
Likelihood and impact use a 1–5 training scale. Inherent score = likelihood × impact. Residual score estimates exposure after the *modeled* existing control; it is not a measured control effectiveness result. Priority: Critical 15–25; High 10–14; Medium 5–9; Low 1–4. The canonical source is `data/risk_register.csv`.

## Executive view
| Priority | Count | Focus |
|---|---:|---|
| Critical | 1 | Finish MFA enrollment for every named user |
| High | 5 | Separate admin work, encrypt/patch endpoints, test restore, narrow shared access |
| Medium | 6 | Protection validation, training, remote access, vendors, incident card, policy approval |
| Total | 12 | Training-only modeled findings |

### Top five modeled risks
1. **R-01 — MFA gap (residual 16):** two modeled users pending enrollment could enable account takeover through stolen passwords.
2. **R-02 — Daily admin use (15):** owner’s routine account could make a successful compromise more consequential.
3. **R-03 — Encryption unknown (12):** loss of a device with sensitive working files may expose data if encryption is absent.
4. **R-04 — Patch delay (12):** delayed updates increase known-vulnerability exposure.
5. **R-05 — Untested restore (12):** backup confidence is incomplete until a restore test succeeds.

## Assumptions and limitations
- Scores are planning heuristics, not actuarial estimates or compliance ratings.
- Observations are simulated from the evidence register, not tenant queries.
- Any real firm must validate assets, data flows, administrative roles, vendor terms, retention rules, and regulatory obligations before acting.

{legal}
""")

write("04_REMEDIATION_ROADMAP.md", f"""# 04 — 30/60/90-Day Remediation Roadmap

{notice}

| Window | Outcome | Finite actions | Owner | Completion evidence |
|---|---|---|---|---|
| Days 0–14 | Close immediate identity gap | Enroll all named users in MFA; record recovery-contact process; pause shared credentials | Owner + Office Manager | Sanitized enrollment roster, recovery-process acknowledgment |
| Days 0–30 | Reduce high-impact workstation/admin exposure | Create separate admin workflow; confirm encryption; patch supported devices; validate endpoint protection | Owner + Office Manager | Role worksheet, device status export, exception list |
| Days 0–30 | Prove recovery path | Select one non-sensitive test item and document a supervised restore validation | Owner + Bookkeeper | Dated restore-test record with pass/fail and follow-up |
| Days 15–45 | Limit access to work need | Approve role/access matrix; review shared-storage groups; remove unneeded access after client approval | Owner + Office Manager | Signed review worksheet and change record |
| Days 15–60 | Establish repeatable operations | Publish remote-access standard, vendor register, incident escalation card, annual training cadence | Owner + Office Manager | Approved drafts, roster, tabletop acknowledgment |
| Days 30–90 | Govern and sustain | Human/legal review policy drafts; schedule quarterly access and backup checks | Owner | Approved policy record and calendar evidence |

## Change-control template
Before each real change: record requester, business reason, system owner, affected users, backup/rollback approach, approval, maintenance window, verifier, result, and unresolved exception. No remediation is authorized by this training file.

## Out-of-scope escalation triggers
Request a separate scope if the client needs tenant migration, endpoint management deployment, 24/7 monitoring, incident response, legal interpretation, extensive cleanup, hardware/software procurement, managed IT, or any testing beyond evidence review.

{legal}
""")

write("05_VERIFICATION_PLAN_AND_RESULTS.md", f"""# 05 — Verification Plan and Simulated Results

{notice}

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

{legal}
""")

write("06_FINAL_CLIENT_PACKAGE.md", f"""# 06 — Final Client Package (Draft)

{notice}

## Draft cover note
LedgerGuard leadership: this training-format package illustrates the output of a limited security-readiness engagement. It is not a live assessment and must not be relied on for operational decisions without real discovery and human/legal review.

## Modeled deliverables
1. Scope and exclusions — `01_SCOPE_AND_RULES_OF_ENGAGEMENT.md`
2. Sanitized evidence register — `02_SIMULATED_EVIDENCE_REGISTER.csv`
3. Twelve-item risk register and prioritization — `03_RISK_ASSESSMENT.md`, `data/risk_register.csv`
4. 30/60/90-day action roadmap — `04_REMEDIATION_ROADMAP.md`
5. Verification protocol/baseline — `05_VERIFICATION_PLAN_AND_RESULTS.md`
6. Implementation-facing handoff — this document

## Modeled leadership decisions
- Name an executive sponsor and operational coordinator.
- Approve a narrowly scoped first change set: MFA, admin separation, device status, and restore validation.
- Confirm who may approve access changes and policy drafts.
- Reserve a 30-day evidence-review meeting before extending scope.

## Acceptance criteria for a real fixed-scope engagement
- Client confirms discovery inputs and asset inventory as sufficiently complete for the stated scope.
- Each finding has an owner, target window, and verification artifact.
- All change recommendations remain recommendations until client approval.
- Legal/policy language has appropriate human/legal review.
- Closeout includes known limitations and separately scoped needs.

## Support boundary
The modeled engagement includes a finite readout and one consolidated clarification round within the agreed window. It excludes ongoing operations, after-hours coverage, unlimited configuration work, and managed IT. Any expanded assistance requires a new written scope.

{legal}
""")

write("07_TIME_AND_COST_TRACKER.csv", """workstream,role,hours_estimated,hours_simulated_actual,rate_hypothesis_usd,amount_hypothesis_usd,status,notes
Discovery and scope,Security lead,5,5,200,1000,Modeled,Interview prep + scope boundary
Evidence normalization,Security lead,4,4,200,800,Modeled,Sanitized register only
Risk assessment and roadmap,Security lead,6,6,200,1200,Modeled,12-item prioritization + 30/60/90 plan
Verification design,Security lead,3,3,200,600,Modeled,No live verification performed
Executive readout and handoff,Security lead,3,3,200,600,Modeled,One finite review round
Project coordination and QA,Security lead,1.5,1.5,200,300,Modeled,Artifact QA and packaging
TOTAL,,22.5,22.5,,4500,Internal hypothesis,Requires market validation; excludes third-party costs
""")

write("08_MVC_DELIVERY_PLAYBOOK.md", f"""# 08 — MVC Delivery Playbook

{notice}

## Minimum viable offer
**Security Readiness Baseline for Small Tax & Accounting Firms** — a fixed-scope, documentation-led engagement for firms that need a prioritized starting point before choosing IT projects. The offering is not managed IT, an audit, a certification, or a promise of compliance.

## Delivery sequence
1. **Qualify (15 min):** firm size, platforms, decision maker, urgent incident check, budget range, and exclusions.
2. **Scope (30 min):** confirm systems, locations, data sensitivity, constraints, deliverables, approvals, and no-access default.
3. **Collect (client-led):** questionnaire and minimum metadata exports; no passwords/taxpayer records.
4. **Analyze (offline):** normalize evidence, score risks, identify assumptions, draft recommendations.
5. **Readout (45 min):** explain top risks, owners, 30/60/90 plan, evidence needed, and separate-scope triggers.
6. **Handoff (one week target):** deliver register, roadmap, verification worksheet, limitations, and next-decision list.
7. **Close (15 min):** one consolidated clarification round; offer separately scoped implementation only if wanted.

## Quality gates
| Gate | Required before proceeding |
|---|---|
| Qualification | No live incident response need; decision maker available; scope fits fixed baseline |
| Contracting | Approved scope, authorized contact, confidentiality/data handling terms |
| Analysis | Evidence marked source/type/date; assumptions and missing items logged |
| Recommendation | Each action has owner, window, verification proof, and out-of-scope tag where needed |
| Delivery | Human/legal review disclaimer retained; all client-specific data redacted/minimized |
| Closeout | Limitations stated; follow-on work separately estimated |

## Capacity model
At the $4,500 hypothesis, modeled effort is 22.5 hours at a $200 blended internal rate. This is an internal planning calculation—not a published price or validated market rate. Do not quote it as proven until discovery calls, competitor positioning, margin targets, and willingness-to-pay feedback validate it.

{legal}
""")

write("09_MVC_ASSETS.md", f"""# 09 — MVC Assets (Internal Drafts)

{notice}

## 1. Cold-call opener (draft)
“I'm developing a limited security-readiness baseline for small tax and accounting firms. It is a short, fixed-scope review of identity, endpoints, backup verification, vendor readiness, and staff processes—not managed IT or a compliance certification. Is reducing operational risk before the next busy season a priority you are already discussing?”

## 2. Discovery questions
1. How many staff, seasonal staff, and firm-owned devices are in the current operating model?
2. Which identity/email platform, tax application, file storage, remote access, and backup services are in use?
3. Who owns administrative access, vendor escalation, and recovery decisions?
4. What evidence exists for MFA, device encryption, updates, endpoint protection, access review, and restore testing?
5. Are there known incidents, contractual requirements, or deadlines that require a different service or urgent response?
6. What internal resource can validate recommendations and approve changes?

## 3. Qualification disqualifiers / redirects
- Active compromise, suspected breach, or lost sensitive data → refer to incident response/legal counsel pathway; do not sell a baseline as the immediate remedy.
- Request for 24/7 monitoring, remote administration, migration, penetration test, or hands-on remediation → separate scope.
- No decision maker, no evidence owner, or expectation of compliance guarantee → pause/decline until resolved.

## 4. One-page proposal skeleton
**Objective:** deliver a prioritized readiness baseline.  
**Inputs:** client-approved questionnaire and minimum metadata.  
**Outputs:** evidence register, risk register, 30/60/90 roadmap, verification worksheet, leadership readout.  
**Timing:** agreed fixed window after inputs are received.  
**Client responsibilities:** provide accurate information, name approver, approve any changes.  
**Exclusions:** legal advice, certifications, pentesting, forensics, 24/7 monitoring, managed IT, major migration, hardware/software costs, unlimited remediation.  
**Investment:** internal hypothesis $4,500, subject to market validation and approved proposal.

## 5. Delivery QA checklist
- [ ] Fiction/training label and legal-review notice present.
- [ ] No client identifiers, taxpayer data, passwords, screenshots of live systems, or credentials.
- [ ] Risk counts reconcile to canonical CSV.
- [ ] Every recommendation has a verification artifact and owner.
- [ ] Scope boundary and separate-scope triggers shown.
- [ ] Pricing framed as unvalidated internal hypothesis.

{legal}
""")

# Portfolio visual HTML. 8 slides supported by query param.
slides = [
("01","Training Simulation Overview","LedgerGuard Tax & Accounting LLC","Fictional seven-person Central Florida firm model","No real tenant · no taxpayer data · no external access","Scope: identity, endpoints, resilience, workflows"),
("02","Evidence Register","14 sanitized evidence records","Identity 3 · Endpoint 3 · Data 3 · Process 5","All source types marked mock / interview-style","No credentials, serials, or personal data retained"),
("03","Risk Prioritization","12 modeled risks","1 Critical · 5 High · 6 Medium","Highest modeled issue: MFA enrollment gap","Scores are planning heuristics, not compliance ratings"),
("04","First 30 Days","Four finite control outcomes","MFA enrollment · separate admin workflow","Encryption/patch posture · restore validation","Each outcome has owner and evidence rule"),
("05","Verification Matrix","8 control checks","Every control has requested evidence and pass rule","Baseline results are intentionally not passed","No live verification was performed"),
("06","Scope Guardrails","What this engagement does not do","No pentesting · forensics · 24/7 monitoring","No migrations · managed IT · legal advice","No certification or security guarantee"),
("07","Delivery MVC","Fixed-scope delivery flow","Qualify → Scope → Client-led collection → Analyze","Readout → Handoff → One clarification round","Internal $4,500 hypothesis requires validation"),
("08","Readiness Gate","Cold-call readiness: NO PASS","Assets and safety boundaries are complete","Market validation, proposal review, and counsel review are pending","Do not quote price as validated or imply live assessment")]
slide_js = json.dumps(slides, ensure_ascii=False)
write("portfolio/portfolio_gallery.html", f"""<!doctype html><html><head><meta charset='utf-8'><title>LedgerGuard Training Portfolio</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#e7ecea;color:#12221e;font-family:Georgia,'Times New Roman',serif}}.frame{{width:1600px;height:900px;padding:70px 88px;background:#f8f5ed;position:relative;overflow:hidden}}.stripe{{position:absolute;top:0;left:0;width:100%;height:18px;background:#1d5145}}.label{{font:700 17px/1.2 Arial,sans-serif;letter-spacing:2px;color:#1d5145;text-transform:uppercase}}h1{{font-size:66px;line-height:1.02;max-width:1040px;margin:52px 0 24px;font-weight:600;letter-spacing:-1.5px}}.firm{{font:600 28px/1.2 Arial,sans-serif;color:#a1542c;margin-bottom:62px}}.grid{{display:grid;grid-template-columns:1fr 1fr;gap:22px;max-width:1240px}}.card{{border-top:2px solid #1d5145;padding:18px 0;font:500 24px/1.38 Arial,sans-serif}}.footer{{position:absolute;left:88px;bottom:50px;font:600 16px Arial,sans-serif;letter-spacing:1px;color:#53615a}}.badge{{position:absolute;right:88px;bottom:44px;border:2px solid #a1542c;color:#8d4524;padding:11px 15px;font:700 14px Arial,sans-serif;letter-spacing:1px}}@media(max-width:1600px){{.frame{{transform-origin:top left}}}}</style></head><body><div class='frame'><div class='stripe'></div><div class='label'>LedgerGuard / portfolio evidence / fictional training</div><h1 id='title'></h1><div class='firm' id='firm'></div><div class='grid' id='grid'></div><div class='footer'>SANITIZED · LOCAL-ONLY · 2026-09-17</div><div class='badge'>NOT CLIENT WORK</div></div><script>const s={slide_js};const p=new URLSearchParams(location.search);const i=Math.max(0,Math.min(s.length-1,(+p.get('slide')||1)-1));const x=s[i];document.title='LedgerGuard Portfolio '+x[0];document.querySelector('#title').textContent=x[1];document.querySelector('#firm').textContent=x[2];document.querySelector('#grid').innerHTML=x.slice(3).map(v=>`<div class='card'>${{v}}</div>`).join('');</script></body></html>""")

write("portfolio/SCREENSHOT_CAPTURE_GUIDE.md", f"""# Screenshot Capture and Manifest

{notice}

The eight images in this folder are **sanitized, locally rendered portfolio visuals** from `portfolio_gallery.html`; they are not screenshots of a real firm, Microsoft 365 tenant, tax platform, endpoint tool, or client meeting.

| File | Slide | Claim supported |
|---|---:|---|
| `01_training_overview.png` | 1 | Local fictional scenario boundary |
| `02_evidence_register.png` | 2 | Sanitized evidence inventory |
| `03_risk_prioritization.png` | 3 | 12-item modeled risk assessment |
| `04_first_30_days.png` | 4 | Prioritized finite roadmap |
| `05_verification_matrix.png` | 5 | Verification design/baseline label |
| `06_scope_guardrails.png` | 6 | Exclusions and scope limits |
| `07_delivery_mvc.png` | 7 | Internal MVC workflow |
| `08_readiness_gate.png` | 8 | Truthful no-pass cold-call gate |

## Capture recipe
Open `portfolio_gallery.html?slide=N` locally at a 1600×900 viewport and capture the viewport. Confirm the footer says `SANITIZED · LOCAL-ONLY` and badge says `NOT CLIENT WORK`. Do not add logos, client names, account names, or live-system data.
""")

write("10_COMPLETION_REPORT.md", f"""# 10 — Completion Report

{notice}

## Completion status
**Artifact package: PASS (local-documentation deliverable).** The simulated engagement package includes scope, evidence, canonical risk data, roadmap, verification plan, draft client handoff, internal cost tracker, MVC workflow/assets, and eight sanitized portfolio images.

## Cold-call readiness gate
**NO PASS — do not represent this offer as market-validated or ready for unsupervised cold-call launch.**

### Reasons for no-pass
1. The $4,500 figure is an internal hypothesis derived from 22.5 modeled hours × $200; no prospect interviews, win/loss data, competitor analysis, margin model, or willingness-to-pay validation has been performed.
2. Proposal terms, data-handling language, disclaimers, and policy references are human/legal review drafts, not approved legal language.
3. The content is fictional and local-only; it does not provide live assessment case studies, client references, or validated outcomes.
4. A real intake workflow still needs an approved agreement, data-minimization process, authorized-contact model, secure evidence channel, and escalation/referral partners for incidents/legal issues.
5. Sales messaging must be reviewed by the service owner to ensure it does not imply certification, regulatory assurance, managed IT, incident response, or guaranteed outcomes.

### What is ready
- A constrained draft value proposition, discovery questions, qualification disqualifiers, delivery sequence, and scope guardrails.
- A training-format sample package that clearly demonstrates expected document structure without misrepresenting actual client work.

### Gate to convert to PASS
Obtain documented owner approval after: (a) 5–10 target-firm discovery conversations; (b) price/positioning validation; (c) human/legal review of agreement and public claims; (d) secure intake/retention workflow; (e) defined referral/escalation path; and (f) one approved pilot with real authorization and evidence handling.

## Verification record
- Expected evidence items: 14 (`02_SIMULATED_EVIDENCE_REGISTER.csv`).
- Expected risk records: 12 (`data/risk_register.csv`) reconciling to 1 Critical / 5 High / 6 Medium.
- Expected portfolio images: 8 PNG files named in `portfolio/SCREENSHOT_CAPTURE_GUIDE.md`.
- No real tenants, external systems, taxpayer data, FamilyConnect source material, or agent profiles were accessed or modified by this simulation generator.

{legal}
""")

write("07_DELIVERY_PROCESS_AND_SCOPE.md", f"""# 07 — Delivery Process and Scope (Internal Sales Draft)

{notice}

## Offer name
Security Readiness Baseline for Small Tax & Accounting Firms.

## Buyer outcome
Give a small accounting-firm owner a prioritized, evidence-aware starting point for reducing common identity, endpoint, backup, access, vendor, and staff-process risks—without selling a broad managed IT contract.

## Fixed-scope process
| Stage | Client interaction | Internal output | Boundary |
|---|---|---|---|
| Qualify | 15-minute fit call | Fit/disqualifier record | Redirect live incidents and managed-service requests |
| Scope | 30-minute call | Approved system list, owners, exclusions | No credentials or taxpayer files |
| Collect | Client-led questionnaire/metadata | Evidence register | No tenant access by default |
| Analyze | Offline review | Risk register + assumptions | No audit/certification claim |
| Readout | 45-minute leadership session | 30/60/90 priorities | Recommendations only |
| Handoff | Fixed delivery window | Roadmap + verification worksheet | One clarification round |

## Deliverables
- Scope and rules of engagement
- Sanitized evidence register
- Prioritized risk register
- 30/60/90-day roadmap
- Verification checklist
- Leadership handoff and known limitations

## Explicit exclusions
No legal advice, certification guarantee, compliance attestation, unlimited remediation, major migration, pentesting, forensics, incident response, 24/7 monitoring, hardware/software costs, or managed IT unless separately scoped in writing.

## Pricing hypothesis and validation
**Internal hypothesis only:** $4,500 for 22.5 modeled hours at a $200 blended internal rate. Do not quote as a validated market price. Validate using target interviews, competitor/alternative analysis, delivery capacity, margin requirements, and a controlled pilot.

## Sales guardrail
Use only the following truthful posture: “We offer a limited readiness baseline, not a compliance certification or managed IT service.” Do not present fictional examples as clients, claim live tenant findings, or imply guaranteed security outcomes.

{legal}
""", sales=True)

print(f"Generated documents under {ROOT} and {SALES}")
