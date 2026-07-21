# Build Knowledge-Enhanced AI Agents with Foundry IQ

This repository demonstrates how Microsoft Foundry IQ, Azure AI Search, Microsoft Sentinel, Microsoft Defender XDR, and structured security knowledge can support an AI-powered enterprise knowledge and threat-hunting assistant. The project began as an enterprise knowledge assistant and was extended with an authorized RemcosRAT malware-analysis and Microsoft Sentinel threat-hunting use case.

> In simple terms, the project demonstrates an AI assistant that can search approved information, explain security evidence, and help analysts investigate suspicious activity without making unsupported claims.

---

## Project Overview

| Area | Capability |
|---|---|
| Enterprise Knowledge | Searches connected organizational documents |
| Grounded AI | Uses approved knowledge sources before answering |
| Microsoft Foundry IQ | Hosts and manages the AI agent |
| Azure AI Search | Retrieves relevant enterprise content |
| Microsoft Sentinel | Stores threat intelligence and supports hunting |
| Microsoft Defender XDR | Provides endpoint, process, file, and network telemetry |
| Threat Hunting | Searches exact IOCs and related behavior |
| Validation | Tests accuracy, consistency, and safety |

The repository combines implementation guidance, a Python SDK example, validation evidence, AI-agent prompts, malware-analysis knowledge, STIX threat intelligence, a behavioral watchlist, and reviewable KQL hunts.

---

## Project Objectives

- Build a grounded enterprise AI assistant
- Connect the agent to approved knowledge
- Support Microsoft Sentinel and Defender investigations
- Validate IOCs without assuming compromise
- Generate reviewable KQL threat hunts
- Maintain human analyst control

For non-technical readers, grounding means the assistant checks approved source material before responding. It helps the AI explain what is known, what is only suspected, and what still requires investigation.

---

## Solution Architecture

![Microsoft Foundry IQ Architecture](images/Azure-AI-Foundry-Diagram.png)

```text
User
  ↓
Microsoft Foundry IQ Agent
  ↓
Approved Knowledge and Azure AI Search
  ↓
Microsoft Sentinel and Defender XDR Evidence
  ↓
Grounded Investigation Response
  ↓
Human Analyst Review
```

The enterprise workflow retrieves approved organizational knowledge through Azure AI Search. The security workflow adds static-analysis knowledge, threat intelligence, watchlist artifacts, and telemetry searches. The agent supports investigation and reporting, but a human analyst remains responsible for conclusions and operational actions.

See the full [architecture documentation](src/architecture.md).

---

## Core Technologies

| Technology | Role in the project |
|---|---|
| Microsoft Foundry IQ | Agent creation, management, grounding, and interaction |
| Azure AI Search | Retrieval of relevant content from connected knowledge |
| Azure AI Projects SDK | Programmatic access to the published agent |
| Azure Identity | Azure-native authentication through `DefaultAzureCredential` |
| Python | SDK integration and validation workflow |
| Microsoft Sentinel | Threat-intelligence storage, watchlists, and hunting |
| Microsoft Defender XDR | Advanced-hunting telemetry for devices, files, processes, and networks |
| KQL | Repeatable security searches and validation queries |
| STIX 2.1 | Portable threat-intelligence indicator packaging |
| YARA | Static file-pattern detection documented in the malware knowledge |

---

## Enterprise Knowledge Assistant

The original implementation connects an enterprise knowledge agent to Azure AI Search and an approved knowledge base. Its instruction model emphasizes:

- Searching connected knowledge before answering
- Returning concise, professional responses
- Using citations when available
- Stating when information is not present
- Avoiding unsupported assumptions

The Python example in [`src/run_agent.py`](src/run_agent.py) uses the Azure AI Projects SDK and `DefaultAzureCredential` to submit validation questions to the configured agent. Environment-specific configuration should be reviewed and sanitized before reuse.

### Why It Matters

Enterprise information is often distributed across policies, procedures, and technical documents. A grounded assistant reduces manual searching and makes answers easier to trace to approved sources.

Detailed setup is available in the [deployment guide](src/deployment-guide.md).

---

## RemcosRAT Threat-Hunting Extension

The security extension converts findings from authorized static analysis of an obfuscated RemcosRAT VBS and PowerShell loader into safe defensive content. It includes:

- Approved malware-analysis knowledge
- Standard threat-intelligence indicators
- A STIX 2.1 bundle for later Sentinel import
- A behavioral-artifact watchlist
- Hash, network, and process hunts
- Threat-intelligence import validation
- IOC-validation and threat-hunting prompts
- Safe screenshots and investigation documentation

The original malware archive, VBS sample, decoded binaries, payloads, credentials, and environment identifiers are not stored in the repository.

### Evidence Boundaries

| Evidence category | Meaning |
|---|---|
| Threat Intelligence | A known warning sign associated with the analyzed sample |
| Static-Analysis Finding | Behavior the sample was designed to perform |
| Exact Environment Match | The exact indicator appeared in internal telemetry |
| Behavioral Similarity | Related activity appeared and needs correlation |
| Confirmed Execution | Internal telemetry supports execution or multiple correlated malicious signals |

Importing an indicator or finding a behavioral term does not prove that a monitored environment was compromised.

Read the complete [RemcosRAT Sentinel integration guide](src/remcosrat/remcosrat-sentinel-integration.md).

---

## RemcosRAT Intelligence and Hunting Assets

### Threat Intelligence

The project separates standard threat-intelligence indicators from behavioral artifacts:

| Asset | Purpose |
|---|---|
| [`remcosrat-iocs.csv`](sentinel/remcosrat/threat-intelligence/remcosrat-iocs.csv) | Source catalog for documented RemcosRAT values |
| [`remcosrat-stix-bundle.json`](sentinel/remcosrat/threat-intelligence/remcosrat-stix-bundle.json) | STIX 2.1 bundle containing SHA-256, SHA-1, MD5, domain, and URL indicators |
| [`remcosrat-behavioral-artifacts.csv`](sentinel/remcosrat/watchlists/remcosrat-behavioral-artifacts.csv) | Watchlist data for filenames, paths, commands, WMI, PowerShell, and .NET artifacts |

The watchlist alias is `RemcosRATBehavioralArtifacts`, with `artifact_value` as its SearchKey. Watchlist entries are reference data and must be correlated with environment telemetry.

### Hunting Queries

| Query | Table | Purpose |
|---|---|---|
| [`remcosrat-hash-hunt.kql`](sentinel/remcosrat/kql/remcosrat-hash-hunt.kql) | `DeviceFileEvents` | Searches exact file and initiating-process hashes |
| [`remcosrat-network-hunt.kql`](sentinel/remcosrat/kql/remcosrat-network-hunt.kql) | `DeviceNetworkEvents` | Searches the documented domain, URL, and downloaded filename |
| [`remcosrat-process-hunt.kql`](sentinel/remcosrat/kql/remcosrat-process-hunt.kql) | `DeviceProcessEvents` | Searches VBS, PowerShell, WMI, decoding, and in-memory loading behavior |
| [`remcosrat-threat-intel-validation.kql`](sentinel/remcosrat/kql/remcosrat-threat-intel-validation.kql) | `ThreatIntelIndicators` | Confirms whether expected indicators exist in Sentinel threat intelligence |

These queries produce investigation leads, not automatic compromise conclusions. Table availability, field schemas, retention, and permissions must be validated in the target Sentinel or Defender environment.

---

## AI Threat Hunt Agent Resources

| Resource | Purpose |
|---|---|
| [RemcosRAT malware knowledge](agent-knowledge/malware/remcosrat-vbs-loader.md) | Approved analysis scope, exact artifacts, execution chain, ATT&CK context, and reporting guidance |
| [IOC-006 validation prompt](prompts/remcosrat/IOC-006-RemcosRAT-IOC-Validation.md) | Structured IOC validation and evidence-classification workflow |
| [HUNT-003 threat-hunt prompt](prompts/remcosrat/HUNT-003-RemcosRAT-Threat-Hunt.md) | Repeatable hunt using validated indicators and behavioral artifacts |
| [Security controls](src/security-controls.md) | Evidence, safety, ingestion, KQL, escalation, and human-review safeguards |

The approved knowledge source gives the agent a stable reference. The prompts tell it how to investigate and structure results. The controls prevent intelligence or static analysis from being misreported as internal execution.

---

## Investigation Workflow

```text
Validate approved source values
  ↓
Prepare or import standard threat intelligence
  ↓
Validate ThreatIntelIndicators ingestion
  ↓
Load behavioral reference data into the watchlist
  ↓
Run hash, network, and process hunts
  ↓
Correlate device, user, time, process, file, network, and alert evidence
  ↓
Document assumptions, unknowns, severity, and confidence
  ↓
Human analyst review and authorized action
```

Analysts should preserve the query time range, relevant table names, device and user context, process ancestry, event identifiers, and telemetry gaps. Records from unrelated devices or time periods must not be combined without evidence linking them.

---

## Validation Results

The original enterprise knowledge workflow documents the following validation results:

| Test ID | Validation item | Documented status |
|---|---|---|
| VT-01 | Azure AI Search lookup | Pass |
| VT-02 | Resource-group validation | Pass |
| VT-03 | Region validation | Pass |
| VT-04 | Knowledge-base retrieval | Pass |
| VT-05 | Document summarization | Pass |
| VT-06 | Agent-name validation | Pass |
| VT-07 | Python SDK execution | Pass |
| VT-08 | Azure authentication | Pass |
| VT-09 | Foundry agent connection | Pass |
| VT-10 | Knowledge-base connection | Pass |

Supporting enterprise screenshots are available in [`images/`](images/). The repository also contains validated JSON, exact-value, structure, and content checks for the RemcosRAT defensive artifacts. These file-level checks do not claim that the KQL was executed in a specific workspace or that malware activity was found.

### Validation Evidence

| Evidence | File |
|---|---|
| Azure AI Search retrieval | [`enterprise-knowledge-agent-test-01.png`](images/enterprise-knowledge-agent-test-01.png) |
| Resource retrieval | [`enterprise-knowledge-agent-test-02.png`](images/enterprise-knowledge-agent-test-02.png) |
| Document summarization | [`enterprise-knowledge-agent-output.png`](images/enterprise-knowledge-agent-output.png) |
| Python SDK example | [`run_agent.py.png`](images/run_agent.py.png) |
| Python execution output | [`output-run-agent.py.png`](images/output-run-agent.py.png) |
| RemcosRAT execution flow | [`RemcosRAT_Diagram.png`](images/remcosrat/RemcosRAT_Diagram.png) |
| Sentinel threat-intelligence validation | [`RemcosRAT_Sentinel_15_Threat_Intelligence_Import_Validation_35610632.png`](images/remcosrat/RemcosRAT_Sentinel_15_Threat_Intelligence_Import_Validation_35610632.png) |

> A screenshot or passing file check supports documentation quality. Analysts must still validate current platform state and telemetry before operational use.

---

## Repository Structure

```text
foundry-iq-agent/
├── README.md
├── LICENSE
├── agent-knowledge/
│   └── malware/
├── images/
│   └── remcosrat/
├── prompts/
│   └── remcosrat/
├── sentinel/
│   └── remcosrat/
│       ├── kql/
│       ├── threat-intelligence/
│       └── watchlists/
└── src/
    ├── architecture.md
    ├── deployment-guide.md
    ├── lessons-learned.md
    ├── run_agent.py
    ├── security-controls.md
    └── remcosrat/
        └── remcosrat-sentinel-integration.md
```

---

## Documentation Guide

| Document | Use it for |
|---|---|
| [Architecture](src/architecture.md) | Components, data flow, authentication, and validation architecture |
| [Deployment Guide](src/deployment-guide.md) | Detailed Foundry, Search, knowledge-base, SDK, and validation procedures |
| [Security Controls](src/security-controls.md) | Evidence standards, safe handling, KQL controls, escalation, and governance |
| [Lessons Learned](src/lessons-learned.md) | Project observations, challenges, recommendations, and future improvements |
| [RemcosRAT Sentinel Integration](src/remcosrat/remcosrat-sentinel-integration.md) | End-to-end threat-intelligence, watchlist, KQL, and SOC workflow |

This README intentionally avoids duplicating the detailed commands, troubleshooting steps, screenshots, and control descriptions in those documents.

---

## Quick Start

### Enterprise Knowledge Workflow

1. Review the [architecture](src/architecture.md) and [deployment guide](src/deployment-guide.md).
2. Prepare Microsoft Foundry IQ, Azure AI Search, and an approved knowledge source.
3. Configure and publish the grounded agent.
4. Install the Azure AI Projects SDK and Azure Identity in an isolated Python environment.
5. Review and adapt [`src/run_agent.py`](src/run_agent.py) without committing environment identifiers or secrets.
6. Run the documented validation tests and preserve safe evidence.

### Security Investigation Workflow

1. Read the [RemcosRAT knowledge source](agent-knowledge/malware/remcosrat-vbs-loader.md).
2. Review the [security controls](src/security-controls.md).
3. Validate the STIX and watchlist files before ingestion.
4. Use approved Sentinel procedures to import intelligence and watchlist data.
5. Confirm ingestion with the threat-intelligence validation query.
6. Run the hash, network, and process hunts in the appropriate Sentinel or Defender context.
7. Correlate results and require human review before action.

Detailed commands and platform procedures are intentionally maintained in the linked guides.

---

## Security and Responsible Use

The project follows these core rules:

- Do not store malware samples, suspicious archives, decoded binaries, or payloads in the repository.
- Do not contact documented malicious infrastructure outside an authorized isolated lab.
- Do not store credentials, keys, tokens, tenant IDs, workspace IDs, subscription IDs, or private customer data.
- Keep standard threat intelligence separate from behavioral watchlists.
- Treat KQL results as evidence requiring interpretation.
- Do not claim compromise without supporting internal telemetry.
- Require human review before isolation, blocking, containment, publication, or closure.

See [Security Controls](src/security-controls.md) for the complete 23-control framework.

---

## Key Lessons

- Knowledge quality strongly influences response quality.
- Azure AI Search improves retrieval and grounding.
- Clear agent instructions reduce unsupported responses.
- Incremental validation catches configuration and content errors early.
- Azure Identity supports safer authentication than embedded credentials.
- Threat intelligence and environment telemetry must remain separate.
- Exact IOC matches and behavioral similarities require different reporting language.
- Human judgment remains essential for escalation and containment.

See [Lessons Learned](src/lessons-learned.md) for detailed observations and recommendations.

---

## Project Status

| Field | Value |
|---|---|
| Status | Complete |
| Version | 1.0 |
| Platform | Microsoft Foundry IQ |
| Cloud provider | Microsoft Azure |
| Primary language | Python |
| Repository | `foundry-iq-agent` |

“Complete” reflects the documented portfolio implementation and repository artifacts. It does not claim production deployment, current cloud-resource availability, Sentinel ingestion in every workspace, or detection of RemcosRAT in an environment.

---

## References

### Project Documentation

- [Architecture](src/architecture.md)
- [Deployment Guide](src/deployment-guide.md)
- [Security Controls](src/security-controls.md)
- [Lessons Learned](src/lessons-learned.md)
- [RemcosRAT Sentinel Integration](src/remcosrat/remcosrat-sentinel-integration.md)

### External Documentation

- [Microsoft Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Microsoft Foundry portal](https://ai.azure.com/)
- [Azure AI Search documentation](https://learn.microsoft.com/azure/search/)
- [Azure AI Projects SDK documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Azure Identity documentation](https://learn.microsoft.com/python/api/overview/azure/identity-readme)
- [Microsoft Sentinel documentation](https://learn.microsoft.com/azure/sentinel/)
- [Microsoft Defender XDR advanced hunting](https://learn.microsoft.com/defender-xdr/advanced-hunting-overview)
- [Kusto Query Language documentation](https://learn.microsoft.com/kusto/query/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [MalwareBazaar](https://bazaar.abuse.ch/)
- [GitHub documentation](https://docs.github.com/)

---

## Author

**James Banday**  
Cloud Engineering | Cybersecurity | AI | Platform Engineering

- Repository: [github.com/jbanday808/foundry-iq-agent](https://github.com/jbanday808/foundry-iq-agent)
- LinkedIn: [James Allen Morta Banday](https://www.linkedin.com/in/james-allen-morta-banday-62a391128/)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Disclaimer

This repository is intended for authorized cybersecurity research, education, enterprise AI development, threat hunting, malware analysis, detection engineering, Microsoft Sentinel investigation, Microsoft Defender XDR investigation, and portfolio demonstration.

All AI-generated findings, KQL queries, threat-intelligence imports, escalation recommendations, and containment recommendations require human validation against actual environment telemetry before operational action. The repository does not claim that any monitored environment was compromised or that the documented malware executed internally.
