# RemcosRAT Microsoft Sentinel Integration

## Purpose

This guide documents how findings from authorized static analysis of an obfuscated RemcosRAT VBS and PowerShell loader were converted into:

- Threat-intelligence indicators
- A behavioral-artifact watchlist
- Microsoft Sentinel hunting queries
- Microsoft Defender XDR hunting queries
- AI Threat Hunt Agent knowledge
- IOC validation prompts
- Threat-hunting prompts
- Safe evidence documentation

The goal is to help analysts search for possible RemcosRAT activity without confusing external intelligence with confirmed internal compromise. All query results and AI-generated conclusions require human analyst validation before operational action.

### Non-Technical Explanation

The project takes clues found during malware analysis and organizes them into warning lists and searches that security tools can use. Adding a warning sign to Microsoft Sentinel does not mean an organization was infected; it means analysts have a known clue they can search for.

---

## What Is RemcosRAT?

RemcosRAT is remote-access malware that may allow an attacker to control a computer, run commands, download additional content, collect information, and hide activity. The analyzed sample used an obfuscated VBS and PowerShell execution chain. Obfuscation means the script was deliberately made difficult to read.

Finding a related indicator or behavior does not prove that RemcosRAT executed in a monitored environment. Internal file, process, network, identity, and alert telemetry must support that conclusion.

### Non-Technical Explanation

RemcosRAT can act like an unauthorized remote-control tool that tries to operate without the user noticing. A clue connected to that tool is a reason to investigate, not proof that a computer was controlled.

---

## Analysis Scope and Safety

- The analysis was authorized.
- Static analysis was performed in an isolated environment.
- The VBS sample was not executed in production.
- No connection was made to the decoded URL during static analysis.
- The original ZIP archive, malicious VBS, and decoded binary payloads are not stored in this repository.
- Only safe screenshots, documentation, IOCs, KQL, STIX content, YARA details, and behavioral artifacts are included.
- The documented domain and URL must not be contacted outside an authorized isolated lab.
- Credentials, secrets, tenant IDs, workspace IDs, subscription IDs, and API keys must not be added to these artifacts.

### Non-Technical Explanation

Static analysis means examining a suspicious file without running it. This allows analysts to understand what the file was designed to do while reducing the chance that it will harm a system or contact a malicious service.

---

## Repository Structure

```text
foundry-iq-agent/
├── agent-knowledge/
│   └── malware/
│       └── remcosrat-vbs-loader.md
├── images/
│   └── remcosrat/
├── prompts/
│   └── remcosrat/
│       ├── HUNT-003-RemcosRAT-Threat-Hunt.md
│       └── IOC-006-RemcosRAT-IOC-Validation.md
├── sentinel/
│   └── remcosrat/
│       ├── kql/
│       │   ├── remcosrat-hash-hunt.kql
│       │   ├── remcosrat-network-hunt.kql
│       │   ├── remcosrat-process-hunt.kql
│       │   └── remcosrat-threat-intel-validation.kql
│       ├── threat-intelligence/
│       │   ├── remcosrat-iocs.csv
│       │   └── remcosrat-stix-bundle.json
│       └── watchlists/
│           └── remcosrat-behavioral-artifacts.csv
└── src/
    └── remcosrat/
        └── remcosrat-sentinel-integration.md
```

| Repository area | Purpose |
|---|---|
| `agent-knowledge/` | Approved malware-analysis context for the AI Threat Hunt Agent |
| `prompts/` | Repeatable IOC-validation and threat-hunting instructions |
| `sentinel/remcosrat/threat-intelligence/` | Indicator catalog and portable STIX 2.1 bundle |
| `sentinel/remcosrat/watchlists/` | Behavioral strings and actions used for correlation |
| `sentinel/remcosrat/kql/` | Executable validation and hunting queries |
| `images/remcosrat/` | Safe visual evidence supporting the analysis |
| `src/remcosrat/` | Implementation and operational documentation |

### Non-Technical Explanation

Each folder has one job. The structure keeps known warning signs, related behaviors, searches, supporting evidence, and instructions separate so analysts and the AI agent can find the correct information quickly.

---

## Evidence Classification Model

The integration uses five evidence categories:

| Category | Meaning | What it does not prove |
|---|---|---|
| Threat-intelligence reputation | An external or approved source associates an exact indicator with malicious activity | That the indicator appeared internally |
| Exact environment match | Internal telemetry contains an exact hash, domain, URL, filename, or path | That the full malware chain executed successfully |
| Behavioral similarity | Internal telemetry resembles a documented command or action | That the activity was malicious or was RemcosRAT |
| Confirmed execution evidence | Correlated telemetry supports file, process, network, decoding, or memory-loading activity | Attribution beyond the available evidence |
| Assumptions and unknowns | Evidence is incomplete, unavailable, or inferred | A confirmed finding |

The agent must never turn threat-intelligence reputation into an unsupported compromise statement. It should report exact IOC results as **Intelligence Match** or **Exact IOC Match**, behavioral results as **Behavioral Similarity**, and execution only when telemetry supports it.

### Non-Technical Explanation

A warning list says what defenders should look for. Security records say what happened inside an organization. The two must be connected with evidence before an analyst can conclude that malware ran.

---

## Validated Threat-Intelligence Indicators

Only hashes, the domain, and the URL are treated as standard threat-intelligence indicators in the STIX bundle.

| Indicator type | Exact value |
|---|---|
| SHA-256 | `356106324c797ba967a2a8cde2156e866fe008332046747866efa82a99e62083` |
| SHA-1 | `7e6fc1213ce2ca016d2d577d09a0c91d9f47a533` |
| MD5 | `4713cea293132831a83cdb6ecf9d7637` |
| Domain | `nameless-scene-7204.uploadeeeesclientess.workers.dev` |
| URL | `https://nameless-scene-7204.uploadeeeesclientess.workers.dev/9VKJ-WXKE-YYQN-63FX/img_xxdd6n.png` |

Safe display form of the URL:

```text
hxxps://nameless-scene-7204[.]uploadeeeesclientess[.]workers[.]dev/9VKJ-WXKE-YYQN-63FX/img_xxdd6n[.]png
```

The original URL must remain available separately for exact telemetry matching. Do not use the defanged value in KQL comparisons or STIX patterns.

### Non-Technical Explanation

The three hashes are unique digital fingerprints for the analyzed file. The domain is an internet destination name, and the URL is the complete address of a specific remote resource.

---

## Threat-Intelligence Packaging

### Indicator Catalog

[`remcosrat-iocs.csv`](../../sentinel/remcosrat/threat-intelligence/remcosrat-iocs.csv) records source, confidence, family, description, type, and value. It serves as a source catalog. Some catalog rows—such as filename, path, environment variable, and YARA rule—are behavioral content and must not be imported as standard STIX threat-intelligence objects.

### STIX 2.1 Bundle

[`remcosrat-stix-bundle.json`](../../sentinel/remcosrat/threat-intelligence/remcosrat-stix-bundle.json) is the portable import artifact. STIX is a standard format for sharing threat information between security tools. The bundle contains:

- One producer identity: `James Banday RemcosRAT Static Analysis`
- One SHA-256 indicator
- One SHA-1 indicator
- One MD5 indicator
- One domain indicator
- One URL indicator

Each indicator uses a STIX 2.1 pattern, confidence `90`, the `malicious-activity` indicator type, a validity period from `2026-07-20T00:00:00.000Z` through `2027-07-20T00:00:00.000Z`, and these labels:

```text
remcosrat
malware
vbs-loader
static-analysis
jbanday
```

The bundle intentionally contains no malware object, relationship, threat actor, attack pattern, raw payload, or behavioral-artifact indicator.

### Import Workflow

1. Validate the JSON syntax and STIX object structure locally.
2. Confirm the bundle contains one identity and five indicators.
3. Confirm all object IDs use UUID version 4 and every `created_by_ref` points to the producer identity.
4. Confirm the five STIX patterns match the approved source values exactly.
5. Import the bundle through the organization's approved Microsoft Sentinel threat-intelligence ingestion workflow.
6. Record the workspace, import time, operator, method, and outcome in an authorized operational record, not in this repository.
7. Run [`remcosrat-threat-intel-validation.kql`](../../sentinel/remcosrat/kql/remcosrat-threat-intel-validation.kql) to confirm the current `ThreatIntelIndicators` table contains the expected values.
8. Review missing, deleted, revoked, inactive, future-valid, or expired records before relying on them.

Microsoft Sentinel interfaces and ingestion methods can change. Analysts must follow current organizational procedures and Microsoft documentation for the target workspace.

### Non-Technical Explanation

The STIX bundle is like a package containing five warning signs. Importing it adds those signs to Sentinel's threat-intelligence database; it does not show that any computer encountered them.

---

## Behavioral-Artifact Watchlist

The behavioral watchlist is stored in [`remcosrat-behavioral-artifacts.csv`](../../sentinel/remcosrat/watchlists/remcosrat-behavioral-artifacts.csv).

| Setting | Exact value |
|---|---|
| Watchlist alias | `RemcosRATBehavioralArtifacts` |
| SearchKey | `artifact_value` |

The watchlist contains these exact artifact values:

| Category | Values |
|---|---|
| Filenames | `WWIvxS4BHi.vbs`, `img_xxdd6n.png` |
| File path | `C:\Users\Public\Downloads\WWIvxS4BHi.vbs` |
| Environment variable | `buckskins` |
| YARA rule | `RemcosRAT_Obfuscated_VBS_Loader` |
| VBScript objects | `Scripting.FileSystemObject`, `Wscript.Shell` |
| WMI namespace and classes | `winmgmts:\\.\root\cimv2`, `Win32_ProcessStartup`, `Win32_Process` |
| PowerShell command | `powershell.exe -NoProfile -Command "Invoke-Expression $env:buckskins"` |
| PowerShell APIs | `New-Object Net.WebClient`, `DownloadData` |
| Decoding function | `FromBase64String` |
| Extraction markers | `IN-`, `-in1` |
| In-memory .NET artifacts | `CurrentDomain`, `OtnmpxnddVnptbN.mpxnddVn`, `Otnmpxn` |

Additional static-analysis artifacts documented in the knowledge and hunting prompt include `WScript.ScriptFullName`, `CopyFile`, `CreateObject`, `GetObject`, `ShowWindow = 0`, `[Array]::Reverse`, and `GetMethod`. They are used by the process hunt but are not separate rows in the current watchlist CSV.

### Watchlist Workflow

1. Review the CSV header and confirm `artifact_value` is present.
2. Create or update the Sentinel watchlist with alias `RemcosRATBehavioralArtifacts`.
3. Select `artifact_value` as the SearchKey.
4. Preserve exact casing, punctuation, quotes, and backslashes during upload.
5. Validate access with this watchlist expression:

```kusto
_GetWatchlist('RemcosRATBehavioralArtifacts')
```

6. Confirm the row count and compare imported `artifact_id`, `artifact_type`, and `artifact_value` fields to the repository CSV.
7. Treat watchlist hits as behavioral leads requiring correlation, not proof of compromise.

### Non-Technical Explanation

The threat-intelligence list stores exact standard warning signs. The watchlist stores related behaviors and distinctive text that may help connect events, but some of those behaviors can also occur during legitimate work.

---

## Validated Static-Analysis Execution Chain

The approved knowledge source documents this exact intended sequence:

```text
User opens malicious VBS
        ↓
VBS copies itself to C:\Users\Public\Downloads\WWIvxS4BHi.vbs
        ↓
PowerShell code is stored in the user variable buckskins
        ↓
WMI launches hidden PowerShell
        ↓
PowerShell downloads img_xxdd6n.png
        ↓
Text is extracted between IN- and -in1
        ↓
Characters are modified and reversed
        ↓
Base64 content is decoded
        ↓
.NET assembly is loaded directly into memory
        ↓
Embedded method is invoked
```

This sequence is a static-analysis finding. It describes intended behavior in the sample and is not evidence that the sequence occurred in a monitored environment.

### Non-Technical Explanation

The chain is a step-by-step description of what the file was built to attempt. Security logs must show those steps on a real device before an analyst can say they happened inside an organization.

---

## Threat-Intelligence Import Validation

[`remcosrat-threat-intel-validation.kql`](../../sentinel/remcosrat/kql/remcosrat-threat-intel-validation.kql) queries the current Microsoft Sentinel `ThreatIntelIndicators` table. It:

- Defines the five expected standard indicators in a `datatable`
- Selects the latest record for each indicator object with `arg_max(TimeGenerated, *) by Id`
- Normalizes observable values before comparison
- Uses a left outer join so missing indicators remain visible
- Reports `Present` or `Missing`
- Evaluates active, expired, deleted, revoked, inactive, future-valid, and non-expiring records
- Marks records that require human review

`Present` confirms that an IOC exists in the threat-intelligence table. It does not confirm a match in endpoint or network telemetry. `Missing` means it was not found in the table at query time; it does not change the external intelligence classification.

### Non-Technical Explanation

This query checks whether Sentinel received all five warning signs. It checks the warning list itself, not whether any device contacted or ran something related to those signs.

---

## Hash Hunt

[`remcosrat-hash-hunt.kql`](../../sentinel/remcosrat/kql/remcosrat-hash-hunt.kql) uses `DeviceFileEvents` over the last 30 days. It compares normalized values in:

- `SHA256`
- `SHA1`
- `MD5`
- `InitiatingProcessSHA256`
- `InitiatingProcessSHA1`
- `InitiatingProcessMD5`

The query identifies whether the match came from the file or the initiating process, returns the exact `MatchedHash`, and labels the result `Exact IOC Match`. Analysts must review the file path, action, initiating process, command line, account, device, and nearby events.

### Non-Technical Explanation

A hash is a file's digital fingerprint. This hunt checks both a file and the program that created or changed it for one of the three known fingerprints.

---

## Network Hunt

[`remcosrat-network-hunt.kql`](../../sentinel/remcosrat/kql/remcosrat-network-hunt.kql) uses `DeviceNetworkEvents` over the last 30 days. It searches normalized remote URLs and initiating-process command lines for:

- `nameless-scene-7204.uploadeeeesclientess.workers.dev`
- `https://nameless-scene-7204.uploadeeeesclientess.workers.dev/9VKJ-WXKE-YYQN-63FX/img_xxdd6n.png`
- `img_xxdd6n.png`

The query assigns these match types:

| MatchType | Meaning | Priority |
|---|---|---|
| `Full URL Match` | The documented complete URL appeared | High |
| `Domain Match` | The documented destination domain appeared | High |
| `Downloaded Filename in URL` | The downloaded filename appeared in a remote URL | Medium |
| `Downloaded Filename in Process Command Line` | The downloaded filename appeared in the network process command | Medium |

A network match must be correlated with the initiating process, user, device, timing, file activity, and response action. It does not prove the payload downloaded or executed successfully.

### Non-Technical Explanation

This hunt checks whether a device record mentions the known internet destination or downloaded filename. A mention is an investigative clue, not automatic proof that malware ran.

---

## Process Hunt

[`remcosrat-process-hunt.kql`](../../sentinel/remcosrat/kql/remcosrat-process-hunt.kql) uses `DeviceProcessEvents` over the last 30 days. It searches current and initiating process data for:

- VBS execution through `wscript.exe` or `cscript.exe`
- `WWIvxS4BHi.vbs` and `C:\Users\Public\Downloads\WWIvxS4BHi.vbs`
- PowerShell staging through `buckskins`
- `powershell.exe -NoProfile -Command "Invoke-Expression $env:buckskins"`
- `wmiprvse.exe` launching `powershell.exe`
- WMI process and hidden-window artifacts
- `New-Object Net.WebClient` and `DownloadData`
- `FromBase64String` and `[Array]::Reverse`
- `CurrentDomain` and `GetMethod`
- `OtnmpxnddVnptbN.mpxnddVn` and `Otnmpxn`
- `img_xxdd6n.png`, `IN-`, and `-in1`
- VBScript objects and file-operation terms

The query gives the most specific, highest-priority behavior a `MatchType`, returns its exact `MatchedArtifact`, assigns `Behavioral Similarity`, and calculates `InvestigationPriority` and `RiskScore`. Risk scores order results for review; they are not proof or a substitute for analyst judgment.

### Non-Technical Explanation

A process is a running program. This hunt looks for programs and commands that resemble individual steps in the documented chain, then ranks the strongest clues first.

---

## Query Execution Workflow

1. Confirm Microsoft Defender XDR endpoint data is connected and the required `DeviceFileEvents`, `DeviceNetworkEvents`, and `DeviceProcessEvents` tables contain recent records.
2. Confirm the analyst has permission to query the target workspace and Defender data.
3. Run the threat-intelligence validation query to verify import status.
4. Run the hash hunt for exact file and initiating-process fingerprints.
5. Run the network hunt for the exact domain, URL, and downloaded filename.
6. Run the process hunt for the staged VBS, WMI, PowerShell, decoding, and in-memory loading artifacts.
7. Record the actual query time, time range, workspace context, and table availability.
8. Correlate results by `DeviceId`, `DeviceName`, user, timestamp, `ReportId`, process ancestry, hash, URL, and alert evidence.
9. Expand the time range only when justified by data retention and the investigation scope.
10. Preserve query results and relevant evidence according to organizational procedures.
11. Require human analyst review before escalation, blocking, isolation, or containment.

The KQL files are designed for Microsoft Sentinel environments where the corresponding Defender XDR tables are available and for Microsoft Defender XDR advanced hunting. Table availability, retention, and permissions must be validated in the target environment.

### Non-Technical Explanation

The workflow first checks that the warning list was loaded, then searches files, network connections, and running programs. Analysts connect related records before deciding what happened.

---

## Correlation and Investigation

For each result, review:

- Device identity and business importance
- User and account context
- Exact timestamp and time zone
- File creation, modification, quarantine, and execution actions
- Parent and initiating process relationships
- Full command lines
- WMI and PowerShell activity
- Network destination, protocol, IP address, and port
- Related alerts and alert evidence
- Similar activity on other devices or accounts
- Whether the action was prevented, blocked, or completed
- Whether a legitimate administrative or software explanation exists
- Telemetry gaps, ingestion delays, and retention limits

Do not combine unrelated records from different devices, users, or time periods into one execution chain without evidence linking them.

### Non-Technical Explanation

One record rarely tells the whole story. Analysts compare who, what, where, and when across several security records to decide whether the clues belong to the same event.

---

## Assessment, Severity, and Confidence

### Classification

Use only:

- **Confirmed Malicious**
- **Suspicious**
- **Benign**
- **Unknown**

### Severity

| Evidence state | Severity |
|---|---|
| IOC exists only in threat intelligence | Informational |
| One uncorrelated behavioral artifact | Low |
| Multiple correlated behaviors | Medium |
| Confirmed malicious execution on one device | High |
| Widespread execution or major business impact | Critical |

### Confidence

| Confidence | Evidence standard |
|---|---|
| Low | Limited, incomplete, or conflicting evidence |
| Medium | Multiple related artifacts without confirmed execution |
| High | Strong telemetry with exact IOC correlation and confirmed malicious behavior |

Severity describes potential or observed impact. Confidence describes how strongly evidence supports the assessment. Neither should be based on external reputation alone.

### Non-Technical Explanation

Severity answers “How serious is this?” Confidence answers “How sure are we?” A known malicious warning sign can be high-confidence intelligence while still being only informational for an environment where no matching activity was found.

---

## MITRE ATT&CK Context

The knowledge source maps these as potential techniques from static analysis:

| Technique | Name |
|---|---|
| T1059.005 | Visual Basic |
| T1059.001 | PowerShell |
| T1047 | Windows Management Instrumentation |
| T1027 | Obfuscated or Compressed Files and Information |
| T1105 | Ingress Tool Transfer |
| T1140 | Deobfuscate or Decode Files or Information |
| T1620 | Reflective Code Loading |

Keep two mappings in an investigation report:

- **Potential Techniques from Static Analysis:** capabilities found in the file.
- **Environment ATT&CK Mapping:** techniques supported by internal telemetry.

Do not report a static-analysis mapping as confirmed environment behavior.

### Non-Technical Explanation

MITRE ATT&CK is a standard dictionary for attacker behavior. It gives teams consistent names for techniques, but a name from file analysis does not prove that the technique occurred on a company device.

---

## AI Threat Hunt Agent Integration

### Knowledge Source

[`remcosrat-vbs-loader.md`](../../agent-knowledge/malware/remcosrat-vbs-loader.md) provides the agent with approved analysis scope, exact indicators, behavioral artifacts, execution-chain context, YARA details, Sentinel and Defender guidance, ATT&CK mappings, safety boundaries, and reporting rules.

### IOC Validation Prompt

[`IOC-006-RemcosRAT-IOC-Validation.md`](../../prompts/remcosrat/IOC-006-RemcosRAT-IOC-Validation.md) directs the agent to validate indicator format and reputation, search internal telemetry, separate intelligence from environment activity, generate Sentinel and Defender KQL, identify gaps, and produce a structured SOC response.

### Threat-Hunting Prompt

[`HUNT-003-RemcosRAT-Threat-Hunt.md`](../../prompts/remcosrat/HUNT-003-RemcosRAT-Threat-Hunt.md) supplies the exact indicators, behavioral artifacts, hunt objective, and documented execution chain for repeatable hunting.

### Required Agent Boundaries

- Never invent query results, devices, users, alerts, or timestamps.
- Never claim compromise from threat intelligence alone.
- Label exact IOC matches separately from behavioral similarities.
- State assumptions, unknowns, time range, and unavailable telemetry.
- Generate queries appropriate to the named Sentinel or Defender context.
- Require human analyst validation before operational action.

### Non-Technical Explanation

The knowledge file tells the AI what is known. The prompts tell it how to investigate and report. The boundaries prevent the AI from filling evidence gaps with guesses.

---

## SOC Reporting Structure

Use this response order:

1. Assessment Note
2. Executive Summary
3. IOC Validation Table
4. Threat Assessment
5. Intelligence Matches
6. Environment Matches
7. Behavioral Observations
8. Confirmed Findings
9. Assumptions and Unknowns
10. MITRE ATT&CK Mapping
11. Detection Opportunities
12. Microsoft Sentinel KQL
13. Microsoft Defender XDR KQL
14. Investigation Recommendations
15. Escalation Recommendation
16. Shift Handoff Summary

Every confirmed finding should identify its source table, query time range, timestamp, device, user, process, observable, and supporting event or alert identifier when available.

### Non-Technical Explanation

A standard report format makes it easier for the next analyst to understand what was searched, what was found, what remains unknown, and what should happen next.

---

## Escalation and Operational Action

Recommend analyst escalation when:

- An exact sample hash appears on an endpoint
- `WWIvxS4BHi.vbs` is created or executed
- The documented domain or URL is contacted
- `wmiprvse.exe` launches suspicious `powershell.exe`
- `buckskins` appears in related PowerShell activity
- Multiple behavioral artifacts correlate on the same device and user
- Supporting Sentinel or Defender alerts exist
- Related activity appears on additional devices
- Telemetry supports in-memory loading or confirmed malicious execution

Do not recommend blocking, isolation, account disablement, or containment solely from external reputation. Preserve evidence and obtain human authorization before operational action.

### Non-Technical Explanation

Escalation means asking a qualified analyst to examine stronger or connected clues. Actions that affect devices or users require verified evidence and human approval.

---

## Safe Evidence Documentation

Safe screenshots are stored in [`images/remcosrat/`](../../images/remcosrat/). The current evidence set covers:

- MalwareBazaar sample details
- VirusTotal SHA-256 verification
- Archive metadata and SHA-256 verification
- Sample extraction and extracted path
- Sample SHA-256 verification
- Obfuscated VBS header
- Base64 URL extraction
- Decoded command-and-control URL
- Self-copy hash verification
- YARA string candidates
- Custom YARA rule
- YARA test results
- RemcosRAT execution-flow diagram

Screenshots must not expose raw malware, Base64 payloads, decoded binaries, credentials, secrets, tenant IDs, workspace IDs, subscription IDs, or API keys. Review images before committing them.

### Non-Technical Explanation

The screenshots support the written analysis without storing dangerous files. They show how conclusions were reached while keeping malware and sensitive organization information out of the repository.

---

## Implementation Checklist

- [ ] Confirm all five standard IOC values match the approved knowledge and prompt files.
- [ ] Validate `remcosrat-stix-bundle.json` as JSON and STIX 2.1 content.
- [ ] Confirm the STIX bundle contains one identity and five indicators.
- [ ] Import the STIX bundle through an approved Sentinel workflow.
- [ ] Run the threat-intelligence validation query.
- [ ] Confirm `RemcosRATBehavioralArtifacts` uses `artifact_value` as SearchKey.
- [ ] Verify all 19 behavioral watchlist rows after upload.
- [ ] Confirm Defender XDR data is available in the relevant Sentinel tables.
- [ ] Run the hash, network, and process hunts.
- [ ] Correlate results by device, user, time, process ancestry, and alert.
- [ ] Document telemetry gaps and query limitations.
- [ ] Apply classification, severity, and confidence based on evidence.
- [ ] Preserve safe evidence and investigation records.
- [ ] Obtain human validation before escalation or containment.

### Non-Technical Explanation

The checklist helps teams complete the integration in a consistent order and prevents a warning-list import from being mistaken for evidence of infection.

---

## Source References

- [RemcosRAT Obfuscated VBS Loader Knowledge](../../agent-knowledge/malware/remcosrat-vbs-loader.md)
- [IOC-006 RemcosRAT IOC Validation](../../prompts/remcosrat/IOC-006-RemcosRAT-IOC-Validation.md)
- [HUNT-003 RemcosRAT Threat Hunt](../../prompts/remcosrat/HUNT-003-RemcosRAT-Threat-Hunt.md)
- [RemcosRAT IOC Catalog](../../sentinel/remcosrat/threat-intelligence/remcosrat-iocs.csv)
- [RemcosRAT STIX 2.1 Bundle](../../sentinel/remcosrat/threat-intelligence/remcosrat-stix-bundle.json)
- [RemcosRAT Behavioral Watchlist](../../sentinel/remcosrat/watchlists/remcosrat-behavioral-artifacts.csv)
- [RemcosRAT Hash Hunt](../../sentinel/remcosrat/kql/remcosrat-hash-hunt.kql)
- [RemcosRAT Network Hunt](../../sentinel/remcosrat/kql/remcosrat-network-hunt.kql)
- [RemcosRAT Process Hunt](../../sentinel/remcosrat/kql/remcosrat-process-hunt.kql)
- [RemcosRAT Threat-Intelligence Validation](../../sentinel/remcosrat/kql/remcosrat-threat-intel-validation.kql)
- [RemcosRAT Safe Evidence Images](../../images/remcosrat/)

## Final Assessment

The repository converts authorized RemcosRAT static-analysis findings into separate, reviewable layers: standard IOCs in STIX, behavioral artifacts in a Sentinel watchlist, exact and behavioral KQL hunts, agent knowledge, structured prompts, and safe evidence documentation.

These materials support Microsoft Sentinel and Microsoft Defender XDR investigation. They do not establish that RemcosRAT executed in any monitored environment. That conclusion requires correlated internal telemetry and human analyst validation.

## Author

James Banday

## Project

AI Threat Hunt Agent in Microsoft Foundry

## Analysis Date

2026-07-20

## Disclaimer

This guide is intended for authorized cybersecurity research, education, IOC validation, threat hunting, detection engineering, Microsoft Sentinel investigation, Microsoft Defender XDR investigation, SOC reporting, and portfolio demonstration. All imports, queries, findings, and operational recommendations must be reviewed by a human analyst and validated against actual telemetry before action.
