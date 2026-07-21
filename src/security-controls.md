# Security Controls

## Project Name

AI Threat Hunt Agent in Microsoft Foundry

## Purpose

This document defines the safeguards used to ensure the AI Threat Hunt Agent supports investigations safely, accurately, consistently, and transparently. The controls apply to:

- Microsoft Foundry
- Microsoft Sentinel
- Microsoft Defender XDR
- IOC investigation
- Threat hunting
- Malware-analysis knowledge
- Detection engineering
- KQL generation
- Threat-intelligence ingestion
- Behavioral watchlists
- SOC reporting

These controls establish evidence standards, handling boundaries, validation requirements, and human decision points. They apply across the project; the RemcosRAT workflow is a documented implementation of the broader framework.

### Non-Technical Explanation

These controls are the rules that keep the AI assistant careful, evidence-based, and under human supervision. They help prevent guesses from being presented as facts or automated actions from being taken without review.

---

## Control 1: Evidence Before Conclusions

### Control

The agent must review available evidence before reaching a conclusion. Evidence may include:

- Alerts
- Device activity
- Process activity
- File activity
- Network activity
- User activity
- Threat intelligence
- Uploaded knowledge
- Malware-analysis findings
- Watchlist matches

The agent must name the evidence source, search time range, and relevant identifiers when available. Isolated clues must not be treated as proof. Missing telemetry, unavailable tables, retention gaps, and conflicting evidence must be documented.

### Non-Technical Explanation

The agent must review the facts before saying that something harmful happened. One clue may start an investigation, but several connected records are usually needed to explain what occurred.

---

## Control 2: No Unsupported Compromise Claims

### Control

The agent must not claim that a device, user, account, or organization is compromised unless internal telemetry supports the conclusion. The agent must not claim without evidence that:

- Malware executed
- A host was infected
- Credentials were stolen
- Persistence was established
- Lateral movement occurred
- Data was exfiltrated
- Multiple systems were affected

Threat-intelligence reputation alone does not prove internal compromise. Static analysis describes what a sample is designed to do, not what occurred in an organization.

### Non-Technical Explanation

A known-dangerous file or website is a warning sign, not proof that the company was attacked. Security records must show that relevant activity occurred internally.

---

## Control 3: Threat Intelligence and Environment Evidence Separation

### Control

The agent must clearly separate:

- External threat-intelligence reputation
- Static-analysis findings
- Exact environment matches
- Behavioral similarities
- Confirmed execution evidence

Use these labels consistently:

| Label | Use | Required interpretation |
|---|---|---|
| Intelligence Match | An approved source associates an indicator with a threat | Does not prove the indicator appeared internally |
| Exact IOC Match | Internal telemetry contains an exact approved indicator | Requires context and false-positive review |
| Behavioral Similarity | Telemetry resembles a documented action or artifact | Requires correlation with additional evidence |
| Confirmed Execution | Internal telemetry supports malicious execution or multiple correlated malicious signals | Must cite supporting records and receive human validation |

Importing a STIX indicator into Microsoft Sentinel proves only that the indicator exists in the threat-intelligence database. It does not prove that the indicator appeared in endpoint or network telemetry.

### Non-Technical Explanation

Adding an item to a warning list is different from finding it on a company computer. The agent must keep those two facts separate.

---

## Control 4: IOC Classification

### Control

Use only these classifications:

| Classification | Meaning |
|---|---|
| Confirmed Malicious | Strong evidence supports malicious activity |
| Suspicious | More investigation is required |
| Benign | Legitimate activity is confirmed |
| Unknown | Evidence is insufficient |

The RemcosRAT sample and documented infrastructure may be classified as malicious intelligence based on authorized static analysis and approved sources, while an organization's compromise status remains unknown until internal evidence is found.

### Non-Technical Explanation

These labels provide a consistent way to describe whether a clue is known bad, suspicious, safe, or still uncertain. The label for a clue is not automatically the label for a device or organization.

---

## Control 5: Severity Assignment

### Control

Use only:

- Informational
- Low
- Medium
- High
- Critical

| Situation | Suggested Severity |
|---|---|
| IOC exists only in threat intelligence | Informational |
| One uncorrelated behavioral artifact | Low |
| Several related behavioral artifacts | Medium |
| Confirmed execution on one device | High |
| Widespread execution or major impact | Critical |

Severity must consider:

- Device role
- User role
- Number of affected systems
- Business impact
- Mission impact
- Execution evidence
- Data sensitivity
- Scope

Any adjustment from the general guidance must be explained.

### Non-Technical Explanation

Severity describes how serious the situation is, not how dangerous the malware is in general. A dangerous malware family can still be only an informational environment finding when it appears solely on an external warning list.

---

## Control 6: Confidence Assignment

### Control

Use only:

- Low
- Medium
- High

| Confidence | Criteria |
|---|---|
| Low | Evidence is limited, indirect, or incomplete |
| Medium | Multiple related findings exist, but execution is not confirmed |
| High | Strong telemetry and exact IOC correlation support the conclusion |

Confidence must be supported by the quantity, quality, consistency, and source of evidence. Confidence and severity must be assessed separately.

### Non-Technical Explanation

Confidence answers, “How sure are we based on the evidence?” Severity answers, “How serious is the situation?”

---

## Control 7: Static Malware-Analysis Safety

### Control

- Perform analysis only in an authorized isolated environment.
- Do not execute malware on production systems.
- Do not browse to decoded malicious URLs.
- Do not download remote payloads outside an authorized isolated lab.
- Do not copy malware samples into GitHub.
- Do not store malicious archives, VBS files, binaries, or decoded payloads in this repository.
- Store only safe screenshots, hashes, IOCs, KQL, STIX content, watchlist content, YARA details, and documentation.
- Defang malicious URLs when displaying them for general review.
- Preserve evidence hashes and analysis notes.

Approved RemcosRAT handling context is documented in [RemcosRAT Knowledge](../agent-knowledge/malware/remcosrat-vbs-loader.md) and the [RemcosRAT Sentinel Integration Guide](remcosrat/remcosrat-sentinel-integration.md).

### Non-Technical Explanation

Suspicious files are examined in a controlled lab and are not placed in the public project. The repository contains safe evidence and defensive information, not working malware.

---

## Control 8: Threat-Intelligence Ingestion Safety

### Control

Only standard, validated indicators should be added to the Sentinel threat-intelligence system. Examples include:

- File hashes
- Domains
- URLs
- IP addresses when validated

Behavioral artifacts such as filenames, paths, commands, environment variables, WMI classes, extraction markers, .NET identifiers, and YARA rule names should normally be stored in a watchlist or knowledge document instead.

Threat-intelligence ingestion requires:

- JSON syntax validation before STIX import
- Verification of object counts
- Verification of indicator values
- Review of expiration dates
- Review of confidence values
- Removal of secrets and identifiers
- Use of current supported Sentinel workflows
- Post-import validation using `ThreatIntelIndicators`

The RemcosRAT STIX bundle contains only SHA-256, SHA-1, MD5, domain, and URL indicator objects. A successful import is an ingestion result, not environment evidence.

### Non-Technical Explanation

The threat-intelligence database stores specific warning signs, while the watchlist stores related suspicious behavior. Loading a warning sign does not mean it was found on a device.

---

## Control 9: Watchlist Safety

### Control

Watchlists are reference data and are not proof of malicious activity.

For the RemcosRAT watchlist:

| Setting | Exact value |
|---|---|
| Watchlist alias | `RemcosRATBehavioralArtifacts` |
| SearchKey | `artifact_value` |

Require:

- Unique artifact IDs
- Valid CSV headers
- No empty required fields
- Human review before upload
- Clear artifact descriptions
- Confidence and source fields
- Separation of behavioral artifacts from standard threat intelligence
- Periodic review and removal of stale artifacts

A watchlist match must be correlated with process, file, network, user, and alert telemetry.

### Non-Technical Explanation

A watchlist is like a reference sheet used to compare security records against suspicious names and actions. A matching word or action can have an innocent explanation.

---

## Control 10: KQL Query Safety

### Control

Generated KQL must:

- Use real table and field names
- Be executable
- Use clear time ranges
- Avoid placeholder indicators
- Avoid fictitious findings
- Avoid conclusions inside the query
- Separate Microsoft Sentinel and Defender XDR contexts
- Clearly identify schema assumptions
- Be reviewed before production use
- Avoid automatically isolating devices or blocking indicators
- Avoid contacting malicious infrastructure
- Avoid exposing secrets

The RemcosRAT KQL files serve these distinct purposes:

| Query | Purpose | Evidence Type |
|---|---|---|
| [`remcosrat-hash-hunt.kql`](../sentinel/remcosrat/kql/remcosrat-hash-hunt.kql) | Search file and initiating-process hash fields | Exact file IOC match |
| [`remcosrat-network-hunt.kql`](../sentinel/remcosrat/kql/remcosrat-network-hunt.kql) | Search the documented domain, URL, and downloaded filename | Exact network IOC or filename match |
| [`remcosrat-process-hunt.kql`](../sentinel/remcosrat/kql/remcosrat-process-hunt.kql) | Search VBS, PowerShell, WMI, decoding, and .NET activity | Behavioral similarity |
| [`remcosrat-threat-intel-validation.kql`](../sentinel/remcosrat/kql/remcosrat-threat-intel-validation.kql) | Confirm expected IOCs exist in `ThreatIntelIndicators` | Threat-intelligence ingestion status |

Hash hunts identify exact file fingerprints. Network hunts identify communication with documented infrastructure. Process hunts identify related execution behavior. Threat-intelligence validation confirms ingestion only.

### Non-Technical Explanation

KQL is a search language used to check security records. A query finds records; an analyst still has to decide what those records mean.

---

## Control 11: Exact IOC Match Review

### Control

When an exact IOC is found, review:

- Device name
- User
- Timestamp
- File path
- File action
- Process command line
- Parent process
- Process hash
- Network activity
- Related alerts
- Whether the activity was blocked
- Whether execution occurred

An exact hash or domain match is important but must be reviewed in context. Analysts must determine whether the event was observed, prevented, quarantined, or completed.

### Non-Technical Explanation

Finding the exact warning sign is serious, but analysts still need to determine what happened around it and whether harmful activity actually ran.

---

## Control 12: Behavioral Match Review

### Control

Behavioral matches must not automatically be classified as malicious. Examples include:

- PowerShell
- WMI
- Base64 decoding
- `Net.WebClient`
- `DownloadData`
- Environment variables
- Public download folders
- Image-extension downloads
- Reflection and in-memory loading

Some of these can appear during legitimate administration or software activity. Require correlation with:

- Process ancestry
- User role
- Device role
- File hashes
- Network destination
- Timing
- Alerts
- Multiple artifacts

For example, the documented RemcosRAT workflow treats `WWIvxS4BHi.vbs`, `C:\Users\Public\Downloads\WWIvxS4BHi.vbs`, and `buckskins` as behavioral artifacts. A match to any one of these values requires the same correlation and false-positive review.

### Non-Technical Explanation

One suspicious action can have a legitimate explanation, so analysts should look for several related warning signs on the same device and around the same time.

---

## Control 13: MITRE ATT&CK Mapping

### Control

Clearly separate:

- **Potential Techniques from Static Analysis**
- **Confirmed Environment ATT&CK Mapping**

Only classify a technique as confirmed environment activity when telemetry supports the behavior. Use the [RemcosRAT Knowledge](../agent-knowledge/malware/remcosrat-vbs-loader.md) document as the authoritative source for its potential techniques. Do not invent attribution or additional techniques.

### Non-Technical Explanation

MITRE ATT&CK is a common dictionary used to describe attacker behavior, but the behavior must actually be observed before it is called confirmed.

---

## Control 14: AI Knowledge-Source Control

### Control

The agent should prioritize approved repository knowledge before relying on general knowledge. Require the agent to:

- Use exact IOC values from approved files
- Avoid changing indicator values
- Separate source facts from inference
- State when evidence is unavailable
- Cite or name the supporting knowledge source
- Avoid treating old intelligence as current without review
- Avoid treating a knowledge document as environment telemetry

Approved RemcosRAT sources include:

- [RemcosRAT Knowledge](../agent-knowledge/malware/remcosrat-vbs-loader.md)
- [IOC-006 RemcosRAT IOC Validation](../prompts/remcosrat/IOC-006-RemcosRAT-IOC-Validation.md)
- [HUNT-003 RemcosRAT Threat Hunt](../prompts/remcosrat/HUNT-003-RemcosRAT-Threat-Hunt.md)
- [RemcosRAT Sentinel Integration](remcosrat/remcosrat-sentinel-integration.md)

### Non-Technical Explanation

The agent uses an approved reference guide so it does not have to guess. The guide supplies context but does not replace current security records.

---

## Control 15: Human Review Before Action

### Control

All AI-generated outputs must be reviewed by a human analyst before actions such as:

- Device isolation
- Domain blocking
- URL blocking
- File deletion
- Account disabling
- Host containment
- Indicator publication
- Incident closure
- Escalation to leadership

The agent supports decision-making but does not replace the analyst. The reviewer must verify evidence, scope, likely impact, and authorization.

### Non-Technical Explanation

The AI is an assistant, while a person remains responsible for the final decision.

---

## Control 16: Escalation Control

### Control

Recommend escalation when evidence supports conditions such as:

- Exact malicious hash on an endpoint
- File creation followed by execution
- Suspicious PowerShell launched through WMI
- Communication with documented malicious infrastructure
- Multiple related artifacts on one device
- Related activity on multiple devices
- Confirmed persistence
- Credential access
- Lateral movement
- Data exfiltration
- Business-critical assets affected

Do not recommend escalation based only on an IOC appearing in external intelligence. Escalation must identify the supporting evidence and remaining uncertainty.

### Non-Technical Explanation

Escalation means sending the case to a more experienced team when several warning signs indicate meaningful risk. A warning-list entry alone is not enough.

---

## Control 17: Containment Control

### Control

Containment recommendations must be proportional to evidence. Before recommending isolation or blocking, review:

- Whether execution is confirmed
- Whether the activity is ongoing
- Whether the device is business critical
- Whether the indicator could be shared infrastructure
- Whether blocking may disrupt legitimate activity
- Whether evidence has been preserved
- Whether an incident-response process has been activated

Containment recommendations must state expected benefits, business risks, evidence basis, and required authorization.

### Non-Technical Explanation

Defensive action can interrupt business systems, so it should be based on verified evidence and approved by a responsible person.

---

## Control 18: Data Protection and Secret Handling

### Control

Do not store or expose:

- Passwords
- Access tokens
- API keys
- Tenant IDs when unnecessary
- Workspace IDs when unnecessary
- Subscription IDs when unnecessary
- Private keys
- Connection strings
- Customer data
- Personal information
- Internal hostnames unless intentionally sanitized
- Malware payloads

Require repository review before committing changes. Recommended checks include:

- `git diff`
- `git status`
- Secret-scanning tools when available
- Manual file review for accidental identifiers

### Non-Technical Explanation

The public repository should show the project without exposing private company, customer, or account information.

---

## Control 19: Repository Safety

### Control

Require:

- No malware samples in GitHub
- No suspicious ZIP archives
- No decoded payloads
- No copied credentials
- Safe relative links
- Clear file naming
- Valid JSON
- Valid CSV
- Reviewable KQL
- Markdown rendering validation
- No broken image links
- No accidental duplicate images
- Git review before commit

Safe RemcosRAT screenshots are stored in [`images/remcosrat/`](../images/remcosrat/). Images must be reviewed for raw payloads, secrets, internal identifiers, and sensitive data before commit.

### Non-Technical Explanation

The repository contains evidence and documentation, not working malware. Its contents should be safe for authorized review and portfolio demonstration.

---

## Control 20: Validation and Regression Testing

### Control

Require structured validation when knowledge, prompts, queries, or indicators change. Validation should include:

- Exact IOC checks
- Markdown heading checks
- JSON parsing
- STIX object validation
- CSV row validation
- Duplicate-ID checks
- KQL content checks
- Relative-link checks
- Prompt consistency checks
- Execution-chain consistency checks
- Human review

The existing validation matrix should be updated when new RemcosRAT tests are formally scored. Do not change the documented score unless the validation matrix is actually updated and recalculated.

Validation must distinguish syntactic checks from live platform execution. For example, parsing JSON proves valid JSON syntax; it does not prove Sentinel accepted an import. Reviewing KQL fields does not replace executing the query in the intended workspace.

### Non-Technical Explanation

Testing checks whether the agent still follows the rules after new information is added. A passing file check is not the same as a successful live security-platform test.

---

## Control 21: False Positive Reduction

### Control

Require the agent to consider:

- Approved administrator scripts
- Software deployment tools
- Management systems
- Device role
- User role
- Parent process
- Digital signatures
- Common PowerShell usage
- Shared cloud infrastructure
- Known internal automation
- Security testing activity

Recommend tuning rather than disabling detections. Tuning decisions must preserve coverage of the documented behavior and be recorded for later review.

### Non-Technical Explanation

A false positive is an alert that looks dangerous but is actually normal. Good tuning helps analysts focus on real threats without turning useful detections off.

---

## Control 22: Documentation and Auditability

### Control

Investigation outputs must clearly document:

- Evidence reviewed
- Queries used
- Indicators searched
- Results found
- Evidence not available
- Assumptions
- Severity
- Confidence
- ATT&CK mapping
- Recommendations
- Escalation decision
- Human reviewer

Findings should be reproducible by another analyst. Record query context, time range, time zone, relevant tables, device and user identifiers, event or alert identifiers, and any schema or retention limitation.

### Non-Technical Explanation

Another analyst should be able to understand what was checked, repeat the work, and see how the conclusion was reached.

---

## Control 23: Shift Handoff

### Control

Shift handoff summaries must include:

- Current status
- Key findings
- Exact IOC matches
- Behavioral matches
- Actions completed
- Pending actions
- Evidence gaps
- Severity
- Confidence
- Recommended next steps
- Escalation status

The handoff must distinguish verified facts from assumptions and must not omit important safety or authorization constraints.

### Non-Technical Explanation

The next analyst should be able to continue the case without starting over or mistaking an unverified clue for a confirmed finding.

---

## RemcosRAT Control Mapping

| Repository Artifact | Security Purpose | Required Review |
|---|---|---|
| [`remcosrat-iocs.csv`](../sentinel/remcosrat/threat-intelligence/remcosrat-iocs.csv) | Source catalog for validated intelligence and related artifacts | Verify values, types, sources, confidence, and correct placement |
| [`remcosrat-stix-bundle.json`](../sentinel/remcosrat/threat-intelligence/remcosrat-stix-bundle.json) | Portable STIX 2.1 package containing five standard IOCs | Validate JSON, UUIDs, object counts, patterns, validity, confidence, and import outcome |
| [`remcosrat-behavioral-artifacts.csv`](../sentinel/remcosrat/watchlists/remcosrat-behavioral-artifacts.csv) | Sentinel watchlist data for related behavioral artifacts | Validate headers, unique IDs, required fields, exact values, and staleness |
| [`remcosrat-hash-hunt.kql`](../sentinel/remcosrat/kql/remcosrat-hash-hunt.kql) | Search file and initiating-process hashes | Validate schema, time range, matches, file context, and execution evidence |
| [`remcosrat-network-hunt.kql`](../sentinel/remcosrat/kql/remcosrat-network-hunt.kql) | Search domain, URL, and downloaded-filename activity | Validate process, device, user, destination, timing, and related file activity |
| [`remcosrat-process-hunt.kql`](../sentinel/remcosrat/kql/remcosrat-process-hunt.kql) | Search VBS, PowerShell, WMI, decoding, and .NET behavior | Validate ancestry, user context, legitimate use, correlations, priority, and risk score |
| [`remcosrat-threat-intel-validation.kql`](../sentinel/remcosrat/kql/remcosrat-threat-intel-validation.kql) | Confirm expected IOCs exist in `ThreatIntelIndicators` | Review present, missing, active, expired, deleted, revoked, and inactive records |
| [`remcosrat-vbs-loader.md`](../agent-knowledge/malware/remcosrat-vbs-loader.md) | Approved static-analysis knowledge for the agent | Verify scope, exact artifacts, evidence boundaries, ATT&CK mappings, and safety statements |
| [`IOC-006-RemcosRAT-IOC-Validation.md`](../prompts/remcosrat/IOC-006-RemcosRAT-IOC-Validation.md) | Structured IOC-validation instructions | Review output requirements, evidence labels, KQL context, and conclusion language |
| [`HUNT-003-RemcosRAT-Threat-Hunt.md`](../prompts/remcosrat/HUNT-003-RemcosRAT-Threat-Hunt.md) | Repeatable threat-hunting prompt | Verify exact indicators, artifacts, objective, and execution chain |
| [`remcosrat-sentinel-integration.md`](remcosrat/remcosrat-sentinel-integration.md) | End-to-end implementation guide | Review workflow, platform assumptions, links, safety boundaries, and human decision points |
| [`images/remcosrat/`](../images/remcosrat/) | Safe visual evidence supporting static analysis | Review for sensitive data, payload content, duplicate files, and accurate captions |

---

## Security Review Checklist

- [ ] Malware samples are excluded from the repository
- [ ] Threat-intelligence values were reviewed
- [ ] STIX JSON syntax was validated
- [ ] STIX object relationships were validated
- [ ] Behavioral CSV headers were validated
- [ ] Behavioral artifact IDs are unique
- [ ] KQL uses valid tables and columns
- [ ] KQL contains no placeholders
- [ ] KQL does not claim compromise
- [ ] Prompts separate intelligence from telemetry
- [ ] Knowledge files contain no secrets
- [ ] Relative links were verified
- [ ] Screenshots contain no sensitive information
- [ ] Human analyst review is documented
- [ ] `git diff` was reviewed before commit

Checkboxes remain open until repository or operational evidence proves completion. A prior validation in another task does not automatically authorize marking a control complete here.

---

## Final Summary

These controls help the AI Threat Hunt Agent remain:

- Evidence-based
- Transparent
- Safe
- Reproducible
- Human supervised
- Appropriate for Sentinel and Defender workflows
- Suitable for authorized malware-analysis knowledge
- Resistant to unsupported conclusions

The RemcosRAT content improves the agent's knowledge and hunting capability but does not prove any monitored environment was compromised. Threat-intelligence ingestion, watchlist matches, and query results must be evaluated separately and correlated with actual environment telemetry.

---

## References

- [RemcosRAT Knowledge](../agent-knowledge/malware/remcosrat-vbs-loader.md)
- [RemcosRAT IOC Validation Prompt](../prompts/remcosrat/IOC-006-RemcosRAT-IOC-Validation.md)
- [RemcosRAT Threat Hunt Prompt](../prompts/remcosrat/HUNT-003-RemcosRAT-Threat-Hunt.md)
- [RemcosRAT Sentinel Integration](remcosrat/remcosrat-sentinel-integration.md)
- [RemcosRAT Threat Intelligence](../sentinel/remcosrat/threat-intelligence/)
- [RemcosRAT Watchlist](../sentinel/remcosrat/watchlists/remcosrat-behavioral-artifacts.csv)
- [RemcosRAT KQL Hunts](../sentinel/remcosrat/kql/)
- [RemcosRAT Evidence Images](../images/remcosrat/)

---

## Author

James Banday

## Project

AI Threat Hunt Agent in Microsoft Foundry

## Disclaimer

This project is intended for authorized cybersecurity research, education, threat hunting, malware analysis, detection engineering, Microsoft Sentinel investigation, Microsoft Defender XDR investigation, and portfolio demonstration.

All AI findings, KQL queries, escalation recommendations, and containment recommendations require human validation against actual environment telemetry before operational action.
