# Deployment Guide

## Project Name

Build Knowledge-Enhanced AI Agents with Foundry IQ

---

## Deployment Overview

This guide provides the complete step-by-step process for deploying a knowledge-enhanced AI agent using:

* Microsoft Foundry IQ
* Azure AI Search
* Azure AI Projects SDK
* Azure Identity
* Python
* Azure CLI

The deployment creates an enterprise AI assistant capable of retrieving information from connected knowledge sources and providing grounded responses.

---

# Phase 1: Environment Preparation

## Step 1: Open PowerShell

Launch PowerShell as Administrator.

Purpose:

* Install dependencies
* Configure Azure authentication
* Execute Python scripts

---

## Step 2: Create Project Directory

### Command Overview

Command:

```powershell
mkdir foundry-agent-test
cd foundry-agent-test
```

Explanation:

* mkdir: Creates project directory
* cd: Changes directory

Summary:

Creates the local project workspace.

---

## Step 3: Install Python

Verify Python installation.

### Command Overview

Command:

```powershell
python --version
```

Explanation:

* python: Launches Python
* --version: Displays installed version

Summary:

Verifies Python is installed.

Expected:

```text
Python 3.11.x
```

---

## Step 4: Install Azure CLI

Verify Azure CLI.

### Command Overview

Command:

```powershell
az version
```

Explanation:

* az: Azure CLI
* version: Displays installed version

Summary:

Verifies Azure CLI installation.

---

## Step 5: Create Virtual Environment

### Command Overview

Command:

```powershell
python -m venv venv
```

Explanation:

* python: Python interpreter
* -m venv: Creates virtual environment
* venv: Environment name

Summary:

Creates isolated Python environment.

---

## Step 6: Activate Virtual Environment

### Command Overview

Command:

```powershell
.\venv\Scripts\Activate.ps1
```

Explanation:

* Activates virtual environment

Summary:

Enables isolated package installation.

Expected:

```text
(venv)
```

appears in PowerShell.

---

## Step 7: Install Azure SDK Packages

### Command Overview

Command:

```powershell
pip install azure-ai-projects azure-identity
```

Explanation:

* azure-ai-projects: Foundry IQ SDK
* azure-identity: Azure authentication library

Summary:

Installs required Python dependencies.

---

## Step 8: Authenticate to Azure

### Command Overview

Command:

```powershell
az login
```

Explanation:

* az login: Opens Azure authentication window

Summary:

Authenticates Azure access.

---

# Phase 2: Deploy Microsoft Foundry Resource

## Step 9: Open Azure AI Foundry

Navigate to:

```text
https://ai.azure.com
```

Sign in using your Azure account.

---

## Step 10: Create Foundry Resource

Create:

| Setting        | Value              |
| -------------- | ------------------ |
| Resource Name  | foundry-iq-jbanday |
| Resource Group | Sentinel-RG        |
| Region         | East US            |

Click:

```text
Create
```

Wait for deployment to complete.

---

## Step 11: Enable New Foundry Experience

Enable:

```text
New Foundry
```

from the portal.

---

# Phase 3: Create Agent

## Step 12: Create Agent

Navigate:

```text
Build
→ Agents
→ Create Agent
```

Configure:

| Setting    | Value                      |
| ---------- | -------------------------- |
| Agent Name | enterprise-knowledge-agent |
| Model      | grok-4.3                   |
| Voice Mode | Disabled                   |

---

## Step 13: Configure Instructions

Use:

```text
You are an enterprise knowledge assistant.

Use the connected knowledge sources to answer questions.

Provide accurate, concise responses based on retrieved information.

Always search the knowledge base before responding.

Include citations when available.

If information is unavailable, respond:

"I don't know based on the available knowledge sources."

Do not make assumptions.
```

Save configuration.

---

## Step 14: Publish Agent

Click:

```text
Publish
```

Verify:

```text
Version 5
```

appears.

---

# Phase 4: Create Azure AI Search

## Step 15: Create Search Resource

Create:

| Setting        | Value            |
| -------------- | ---------------- |
| Service Name   | caremedix-search |
| Resource Group | Sentinel-RG      |
| Region         | East US          |

Deploy service.

---

# Phase 5: Create Knowledge Base

## Step 16: Create Knowledge Base

Navigate:

```text
Knowledge
→ Add
→ Create Knowledge Base
```

Configure:

| Setting | Value           |
| ------- | --------------- |
| Name    | knowledgebase42 |

---

## Step 17: Upload Knowledge Sources

Upload:

* Policies
* Procedures
* Technical Documentation
* Deployment Guides

Example:

```text
Build knowledge-enhanced AI agents with Foundry IQ.docx
```

---

## Step 18: Configure Embedding Model

Select:

```text
text-embedding-3-small
```

Create the knowledge base.

---

## Step 19: Connect Knowledge Base

Navigate:

```text
Agent
→ Knowledge
→ Add
```

Select:

```text
knowledgebase42
```

Save configuration.

---

# Phase 6: Agent Validation

## Step 20: Test Agent in Foundry Playground

Example Questions:

```text
What is the service name of the Azure AI Search resource?
```

Expected Response:

```text
caremedix-search
```

---

Question:

```text
What resource group was used?
```

Expected Response:

```text
Sentinel-RG
```

---

Question:

```text
What region was selected?
```

Expected Response:

```text
East US
```

---

Question:

```text
Summarize the uploaded document.
```

Expected Response:

Grounded summary generated from uploaded document.

---

# Validation Screenshots

## Figure 1: Azure AI Foundry Workflow

![Azure AI Foundry Workflow](../images/Azure-AI-Foundry-Diagram.png)

---

## Figure 2: Azure AI Search Validation

![Azure AI Search Validation](../images/enterprise-knowledge-agent-test-01.png)

---

## Figure 3: Resource Validation

![Resource Validation](../images/enterprise-knowledge-agent-test-02.png)

---

## Figure 4: Document Summarization Validation

![Document Summarization](../images/enterprise-knowledge-agent-output.png)

---

# Deployment Success Criteria

| Validation                     | Result  |
| ------------------------------ | ------- |
| Foundry Resource Created       | Success |
| Agent Published                | Success |
| Knowledge Base Connected       | Success |
| Azure AI Search Connected      | Success |
| Search Queries Working         | Success |
| Document Summarization Working | Success |
| Python SDK Integration Working | Success |

---

# Deployment Summary

This deployment creates an enterprise knowledge-enhanced AI assistant using Microsoft Foundry IQ and Azure AI Search.

The deployed solution enables:

* Knowledge retrieval
* Enterprise search
* Document summarization
* Grounded AI responses
* Python SDK integration
* Future enterprise application integration
