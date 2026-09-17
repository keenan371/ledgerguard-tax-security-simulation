# 03 — Risk Assessment

**FICTIONAL TRAINING SIMULATION — NO REAL TENANT, CLIENT, TAXPAYER, OR SYSTEM WAS ACCESSED.**

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

**Human/legal review draft:** This material is operational training content, not legal, tax, compliance, certification, or insurance advice.
