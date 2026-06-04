# Build Knowledge-Enhanced AI Agents with Foundry IQ

## Project Overview

This project provides a complete step-by-step guide for building a knowledge-enhanced AI agent using Microsoft Foundry IQ, Azure AI Search, Azure AI Projects SDK, Azure Identity, and a connected enterprise knowledge base.

The goal is to create an enterprise AI assistant capable of:

* Searching enterprise knowledge sources
* Retrieving relevant information
* Answering questions accurately
* Summarizing uploaded documents
* Providing grounded responses
* Reducing unsupported AI-generated content
* Integrating with Azure AI Search

---

## Business Objectives

Organizations often store critical information across documents, policies, procedures, and knowledge repositories.

This project demonstrates how to:

* Build an enterprise knowledge assistant
* Connect AI agents to organizational knowledge
* Improve information discovery
* Reduce manual searches
* Enhance response accuracy
* Provide secure access to enterprise content

---

## Architecture Overview

### Solution Components

The solution consists of the following Azure services and components:

| Component             | Purpose                       |
| --------------------- | ----------------------------- |
| Microsoft Foundry IQ  | AI Agent Platform             |
| Azure AI Search       | Enterprise Search Engine      |
| Knowledge Base        | Enterprise Content Repository |
| Azure AI Projects SDK | Agent Connectivity            |
| Azure Identity        | Authentication                |
| Azure CLI             | Azure Administration          |
| Python                | Automation and Testing        |

---

## High-Level Architecture

```text
User
 │
 ▼
Enterprise Knowledge Agent
 │
 ▼
Microsoft Foundry IQ
 │
 ▼
Knowledge Base
 │
 ▼
Azure AI Search
 │
 ▼
Enterprise Documents
 │
 ▼
Response Returned to User
```

---

## Figure 1: Azure AI Foundry End-to-End Workflow

Description:

Illustrates the complete Microsoft Foundry IQ workflow from resource creation through AI agent deployment, knowledge integration, testing, and validation.

References:

AWS Pricing Calculator User Guide: This guide provides detailed instructions on using the AWS Pricing Calculator to estimate costs for different AWS services.

![Azure AI Foundry Workflow](images/Azure-AI-Foundry-Diagram.png)

---

## Folder Structure

```text
foundry-iq-agent/
│
├── README.md
│
├── images/
│   ├── Azure-AI-Foundry-Diagram.png
│   ├── enterprise-knowledge-agent-test-01.png
│   ├── enterprise-knowledge-agent-test-02.png
│   ├── enterprise-knowledge-agent-output.png
│   ├── run_agent.py.png
│   └── output-run-agent.py.png
│
└── src/
    ├── architecture.md
    ├── deployment-guide.md
    ├── index.html
    ├── lessons-learned.md
    ├── security-controls.md
    └── run_agent.py
```

---

## Folder Overview

| Folder/File          | Description                        |
| -------------------- | ---------------------------------- |
| README.md            | Main project documentation         |
| images               | Screenshots and validation results |
| architecture.md      | Solution architecture              |
| deployment-guide.md  | Deployment procedures              |
| lessons-learned.md   | Findings and recommendations       |
| security-controls.md | Security requirements              |
| run_agent.py         | Python SDK integration example     |

---

# GitHub Repository Setup

## Step 1: Create the GitHub Repository

Go to:

```text
https://github.com/jbanday808?tab=repositories
```

Select:

```text
New
```

Repository Name:

```text
foundry-iq-agent
```

Description:

```text
Build Knowledge-Enhanced AI Agents with Foundry IQ, Azure AI Search, Azure AI Projects SDK, and Enterprise Knowledge Bases.
```

Visibility:

```text
Public
```

License:

```text
MIT License
```

Click:

```text
Create Repository
```

---

## Step 2: Clone the GitHub Repository

### Command Overview

Command:

```powershell
git clone https://github.com/jbanday808/foundry-iq-agent.git
```

Explanation:

* git clone: Downloads a GitHub repository.
* URL: Repository location.

Summary:

Downloads the Foundry IQ repository to the local workstation.

---

### Command Overview

Command:

```powershell
cd foundry-iq-agent
```

Explanation:

* cd: Changes directory.
* foundry-iq-agent: Repository folder.

Summary:

Navigates into the project directory.

---

# Microsoft Foundry Deployment

## Step 3: Create Microsoft Foundry Resource

Open Azure Portal:

```text
https://portal.azure.com
```

Search:

```text
Foundry
```

Select:

```text
Create a Resource
```

Resource Group:

```text
Sentinel-RG
```

Resource Name:

```text
foundry-iq-jbanday
```

Region:

```text
East US
```

Project Name:

```text
proj-default
```

Select:

```text
Review + Create
```

Then:

```text
Create
```

---

## Step 4: Launch Microsoft Foundry

Select:

```text
foundry-iq-jbanday/proj-default
```

Click:

```text
Go to Foundry Portal
```

---

## Step 5: Enable New Foundry Experience

At the top of the portal:

Enable:

```text
New Foundry
```

---

## Step 6: Create AI Agent

Select:

```text
Start Building
```

Agent Name:

```text
enterprise-knowledge-agent
```

Click:

```text
Create
```

---

## Step 7: Configure Agent Instructions

Paste the following instructions:

```text
You are an enterprise knowledge assistant.

Use the connected knowledge base to answer questions accurately.

Always search the knowledge base before responding.

Provide concise and professional answers.

Include citations when available.

If the requested information is not found in the knowledge base, respond:

"I don't know based on the available knowledge sources."

Do not make assumptions or generate unsupported information.
```

---

# Azure AI Search Deployment

## Step 8: Create Azure AI Search

Return to Azure Portal.

Search:

```text
AI Search
```

Click:

```text
Create
```

Resource Group:

```text
Sentinel-RG
```

Service Name:

```text
caremedix-search
```

Region:

```text
East US
```

Click:

```text
Review + Create
```

Then:

```text
Create
```

---

# Knowledge Base Configuration

## Step 9: Create Knowledge Base

Navigate to:

```text
Knowledge
```

Select:

```text
Add
```

Choose:

```text
Connect to Foundry IQ
```

Foundry Resource:

```text
caremedix-search
```

Authentication:

```text
API Key
```

Click:

```text
Connect
```

Knowledge Base Name:

```text
enterprise-kb
```

Description:

```text
Enterprise knowledge base for policies, procedures, technical documentation, and business information.
```

Embedding Model:

```text
text-embedding-3-small
```

Click:

```text
Create
```

---

## Step 10: Connect Knowledge Base to Agent

Navigate to:

```text
Agents
```

Select:

```text
enterprise-knowledge-agent
```

Under Knowledge:

```text
Add
```

Choose:

```text
Connect to Foundry IQ
```

Select:

```text
knowledgebase42
```

Click:

```text
Connect
```

Then:

```text
Save
```

Finally:

```text
Publish
```

---

## Validation Test #1

Question:

```text
What is the service name of the Azure AI Search resource?
```

Expected Response:

```text
caremedix-search
```

---

## Validation Test #2

Question:

```text
Summarize the uploaded document.
```

Expected Result:

The agent successfully summarizes the uploaded enterprise document using Azure AI Search and the connected knowledge base.

---

## Screenshots

### Figure 2: Azure AI Search Validation

Description:

Shows the enterprise-knowledge-agent successfully retrieving the Azure AI Search service name from the connected knowledge base.

![Azure AI Search Validation](images/enterprise-knowledge-agent-test-01.png)

---

### Figure 3: Resource Validation

Description:

Shows the enterprise-knowledge-agent successfully identifying the Azure Resource Group and deployment region.

![Resource Validation](images/enterprise-knowledge-agent-test-02.png)
```

---

### Figure 4: Document Summarization Validation

Description:

Demonstrates successful document summarization using the connected enterprise knowledge base.

![Document Summarization](images/enterprise-knowledge-agent-output.png)
```

---

# PowerShell, Python, and Azure Configuration

## Step 11: Open PowerShell

Open PowerShell as Administrator.

### Procedure

1. Open Windows Search.
2. Type:

```text
PowerShell
```

3. Right-click:

```text
Windows PowerShell
```

4. Select:

```text
Run as Administrator
```

---

## Figure 5: PowerShell Environment

Description:

Shows the PowerShell environment used to deploy and test the Foundry IQ solution.

![PowerShell Environment](images/output-run-agent.py.png)
```

---

# Project Folder Creation

## Step 12: Create Project Folder

### Command Overview

Command:

```powershell
mkdir foundry-agent-test
```

Explanation:

* mkdir: Creates a directory.
* foundry-agent-test: Project folder name.

Summary:

Creates the local Foundry IQ project directory.

---

### Command Overview

Command:

```powershell
cd foundry-agent-test
```

Explanation:

* cd: Changes directory.
* foundry-agent-test: Target folder.

Summary:

Navigates into the project directory.

---

# Python Installation

## Step 13: Install Python

Download:

```text
Python 3.14.x (64-bit)
```

Official Download Page:

```text
https://www.python.org/downloads/windows/
```

### Installation Options

Select:

```text
Install Now
```

Enable:

```text
Disable Path Length Limit
```

### Verify Installation

#### Command Overview

Command:

```powershell
python --version
```

Explanation:

* python: Python interpreter.
* --version: Displays version.

Summary:

Verifies Python installation.

---

# Azure AI Projects SDK Installation

## Step 14: Install Foundry SDK

### Command Overview

Command:

```powershell
pip install azure-ai-projects azure-identity
```

Explanation:

* pip install: Installs Python packages.
* azure-ai-projects: Azure AI Projects SDK.
* azure-identity: Azure authentication library.

Summary:

Installs the required Azure SDK packages.

---

### Command Overview

Command:

```powershell
python.exe -m pip install --upgrade pip
```

Explanation:

* python.exe: Executes Python.
* -m pip: Runs pip module.
* --upgrade: Updates package.
* pip: Python package manager.

Summary:

Upgrades pip to the latest version.

---

# Python SDK Integration

## Step 15: Create run_agent.py

Create:

```text
run_agent.py
```

---

## Full Python Script

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = "https://foundry-iq-jbanday.services.ai.azure.com/api/projects/proj-default"

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

my_agent = "enterprise-knowledge-agent"
my_version = "5"

openai_client = project_client.get_openai_client()

questions = [
    "What is the service name of the Azure AI Search resource?",
    "Summarize the uploaded document."
]

for question in questions:
    response = openai_client.responses.create(
        input=[
            {
                "role": "user",
                "content": question
            }
        ],
        extra_body={
            "agent_reference": {
                "name": my_agent,
                "version": my_version,
                "type": "agent_reference"
            }
        },
    )

    print("\n----------------------------------------")
    print(f"Question: {question}")
    print(f"Response output: {response.output_text}")
```

---

## Figure 6: Python SDK Integration

Description:

Displays the Python SDK code used to connect to Microsoft Foundry IQ and interact with the enterprise knowledge agent.


```markdown
![Python SDK Integration](images/run_agent.py.png)
```

---

# Azure CLI Installation

## Step 16: Install Azure CLI

Documentation:

```text
https://learn.microsoft.com/cli/azure/install-azure-cli-windows
```

### Verify Installation

#### Command Overview

Command:

```powershell
az version
```

Explanation:

* az: Azure CLI.
* version: Displays installed version.

Summary:

Verifies Azure CLI installation.

---

# Azure Authentication

## Step 17: Sign In to Azure

### Command Overview

Command:

```powershell
az login
```

Explanation:

* az: Azure CLI.
* login: Authenticates to Azure.

Summary:

Signs into Azure.

---

### Verify Authentication

#### Command Overview

Command:

```powershell
az account show
```

Explanation:

* az account: Azure account information.
* show: Displays active subscription.

Summary:

Verifies Azure authentication.

---

# Virtual Environment Configuration

## Step 18: Create Virtual Environment

### Verify Python Installation

#### Command Overview

Command:

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python314\python.exe" --version
```

Explanation:

* &: Executes command.
* python.exe: Python interpreter.
* --version: Displays version.

Summary:

Verifies Python installation.

---

### Create Virtual Environment

#### Command Overview

Command:

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python314\python.exe" -m venv venv
```

Explanation:

* python.exe: Python interpreter.
* -m venv: Creates virtual environment.
* venv: Virtual environment folder.

Summary:

Creates a Python virtual environment.

---

### Enable PowerShell Script Execution

#### Command Overview

Command:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Explanation:

* Set-ExecutionPolicy: Modifies PowerShell execution policy.
* RemoteSigned: Allows local scripts.
* CurrentUser: Applies to current user.

Summary:

Allows PowerShell virtual environment activation.

---

### Activate Virtual Environment

#### Command Overview

Command:

```powershell
.\venv\Scripts\Activate.ps1
```

Explanation:

* venv: Virtual environment folder.
* Activate.ps1: Activation script.

Summary:

Activates the Python virtual environment.

---

# Agent Execution

## Step 19: Run the Agent

### Command Overview

Command:

```powershell
python run_agent.py
```

Explanation:

* python: Executes Python.
* run_agent.py: Agent integration script.

Summary:

Runs the enterprise knowledge agent.

---

## Expected Output

```text
----------------------------------------
Question: What is the service name of the Azure AI Search resource?

Response output:
caremedix-search

----------------------------------------
Question: Summarize the uploaded document.

Response output:
<Document Summary>
```

---

# Agent Validation

## Step 20: Validate Enterprise Knowledge Agent

Open:

```text
https://ai.azure.com/
```

Ask:

```text
What is the name of the agent?
```

Expected Response:

```text
enterprise-knowledge-agent
```

---

Ask:

```text
What resource group was used?
```

Expected Response:

```text
Sentinel-RG
```

---

Ask:

```text
What region was selected?
```

Expected Response:

```text
East US
```

---

## Figure 7: Python Execution Results

Description:

Shows successful execution of run_agent.py and validation of responses returned from the enterprise knowledge agent.


![Python Execution Results](images/output-run-agent.py.png)
```

---

# Complete Command Reference

## Foundry SDK Commands

```powershell
pip install azure-ai-projects azure-identity
python.exe -m pip install --upgrade pip
```

---

## Azure CLI Commands

```powershell
az version
az login
az account show
```

---

## Python Virtual Environment Commands

```powershell
python -m venv venv

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

.\venv\Scripts\Activate.ps1
```

---

## Python Execution Command

```powershell
python run_agent.py
```

---

# Validation Testing

## Validation Test Matrix

| Test ID | Validation Item           | Expected Result                       | Status |
| ------- | ------------------------- | ------------------------------------- | ------ |
| VT-01   | Azure AI Search Lookup    | caremedix-search returned             | Pass   |
| VT-02   | Resource Group Validation | Sentinel-RG returned                  | Pass   |
| VT-03   | Region Validation         | East US returned                      | Pass   |
| VT-04   | Knowledge Base Retrieval  | Knowledge source referenced           | Pass   |
| VT-05   | Document Summarization    | Summary successfully generated        | Pass   |
| VT-06   | Agent Name Validation     | enterprise-knowledge-agent returned   | Pass   |
| VT-07   | Python SDK Execution      | Agent response displayed              | Pass   |
| VT-08   | Azure Authentication      | Azure CLI authentication successful   | Pass   |
| VT-09   | Foundry Agent Connection  | Agent connected successfully          | Pass   |
| VT-10   | Knowledge Base Connection | Knowledge base connected successfully | Pass   |

---

# Validation Questions

## Validation Question 1

Question:

```text
What is the service name of the Azure AI Search resource?
```

Expected Response:

```text
caremedix-search
```

---

## Validation Question 2

Question:

```text
What resource group was used?
```

Expected Response:

```text
Sentinel-RG
```

---

## Validation Question 3

Question:

```text
What region was selected?
```

Expected Response:

```text
East US
```

---

## Validation Question 4

Question:

```text
What is the name of the agent?
```

Expected Response:

```text
enterprise-knowledge-agent
```

---

## Validation Question 5

Question:

```text
Summarize the uploaded document.
```

Expected Response:

```text
Document summary generated from the connected knowledge base.
```

---

# Screenshot Validation

## Figure 8: Azure AI Search Validation

Description:

Shows successful retrieval of the Azure AI Search service name from the connected knowledge base.

References:

AWS Pricing Calculator User Guide: This guide provides detailed instructions on using the AWS Pricing Calculator to estimate costs for different AWS services.

```markdown
![Azure AI Search Validation](images/enterprise-knowledge-agent-test-01.png)
```

---

## Figure 9: Resource Validation

Description:

Shows successful retrieval of deployment resource information from the connected knowledge base.


![Resource Validation](images/enterprise-knowledge-agent-test-02.png)
```

---

## Figure 10: Document Summarization Validation

Description:

Shows successful document summarization using the enterprise knowledge base.

References:

AWS Pricing Calculator User Guide: This guide provides detailed instructions on using the AWS Pricing Calculator to estimate costs for different AWS services.

```markdown
![Document Summarization Validation](images/enterprise-knowledge-agent-output.png)
```

---

# Security Controls

## Identity and Access Management

### Azure Authentication

The solution uses Azure authentication through Azure CLI and Azure Identity.

Benefits:

* Secure authentication
* Role-based access control
* Enterprise identity integration

---

### Azure Identity SDK

Used Component:

```text
DefaultAzureCredential()
```

Purpose:

* Secure token acquisition
* Azure service authentication
* Managed identity support

---

## Access Controls

### Knowledge Base Security

Controls:

* Azure RBAC
* API Key Authentication
* Resource Group Isolation
* Subscription-Level Security

---

### Azure AI Search Security

Controls:

* Search Service Access Control
* API Key Protection
* Network Restrictions
* Azure Authentication

---

## Secure Development Practices

Implemented Controls:

* No hardcoded passwords
* No embedded credentials
* Azure-based authentication
* Least privilege access
* Controlled resource access

---

# Troubleshooting Guide

## Issue: Azure CLI Not Found

Error:

```text
'az' is not recognized as an internal or external command
```

Resolution:

Install Azure CLI.

Verification:

### Command Overview

Command:

```powershell
az version
```

Summary:

Verifies Azure CLI installation.

---

## Issue: Python Not Found

Error:

```text
python is not recognized as an internal or external command
```

Resolution:

Reinstall Python and enable:

```text
Add Python to PATH
```

Verification:

### Command Overview

Command:

```powershell
python --version
```

Summary:

Verifies Python installation.

---

## Issue: Virtual Environment Activation Fails

Error:

```text
Running scripts is disabled on this system.
```

Resolution:

### Command Overview

Command:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Summary:

Allows PowerShell script execution.

---

## Issue: Azure Authentication Failure

Error:

```text
Authentication failed
```

Resolution:

### Command Overview

Command:

```powershell
az login
```

Summary:

Authenticates to Azure.

---

## Issue: Agent Does Not Return Data

Potential Causes:

* Agent not published
* Knowledge base disconnected
* Azure AI Search unavailable
* Authentication issue

Resolution Steps:

1. Verify Azure AI Search status.
2. Verify agent publication.
3. Verify knowledge base connection.
4. Verify Azure authentication.
5. Re-run validation tests.

---

# Lessons Learned

## Lesson 1

Knowledge-enhanced AI agents provide significantly better responses when connected to enterprise knowledge sources.

---

## Lesson 2

Azure AI Search improves retrieval accuracy and helps reduce unsupported AI responses.

---

## Lesson 3

Microsoft Foundry IQ simplifies enterprise AI agent deployment and management.

---

## Lesson 4

Validation testing should always be performed before production deployment.

---

## Lesson 5

Grounded responses improve user trust and response reliability.

---

## Lesson 6

Azure AI Projects SDK simplifies programmatic interaction with enterprise AI agents.

---

# Best Practices

## Authentication

Use:

```python
DefaultAzureCredential()
```

Benefits:

* Secure authentication
* Azure-native integration
* Managed identity support

---

## Knowledge Management

Recommendations:

* Maintain current documents.
* Remove outdated information.
* Validate knowledge sources regularly.
* Monitor retrieval accuracy.

---

## Agent Design

Recommendations:

* Use clear instructions.
* Require knowledge retrieval.
* Prevent unsupported responses.
* Enable validation testing.

---

# References

## Microsoft Foundry Documentation

https://learn.microsoft.com/azure/ai-foundry/

https://ai.azure.com/

---

## Azure AI Search Documentation

https://learn.microsoft.com/azure/search/

https://learn.microsoft.com/azure/search/search-create-service-portal

---

## Azure AI Projects SDK Documentation

https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme

https://pypi.org/project/azure-ai-projects/

---

## Azure Identity Documentation

https://learn.microsoft.com/python/api/overview/azure/identity-readme

https://pypi.org/project/azure-identity/

---

## Azure CLI Documentation

https://learn.microsoft.com/cli/azure/

https://learn.microsoft.com/cli/azure/install-azure-cli-windows

---

## Python Documentation

https://www.python.org/downloads/

https://docs.python.org/3/library/venv.html

https://pip.pypa.io/en/stable/

---

## GitHub Documentation

https://docs.github.com/

https://git-scm.com/download/win

---

## Project Source Material

Build Knowledge-Enhanced AI Agents with Foundry IQ Deployment Guide

Description:

This project was developed using the deployment procedures, Python SDK integration examples, validation tests, and workflow documentation from the Build Knowledge-Enhanced AI Agents with Foundry IQ guide.

---

# Final Repository Validation Checklist

## Repository Structure

* [ ] README.md uploaded
* [ ] images folder uploaded
* [ ] src folder uploaded
* [ ] run_agent.py uploaded

---

## Documentation Validation

* [ ] Deployment guide completed
* [ ] Architecture documented
* [ ] Security controls documented
* [ ] Lessons learned documented
* [ ] References added

---

## Functional Validation

* [ ] Agent created
* [ ] Knowledge base connected
* [ ] Azure AI Search operational
* [ ] Validation tests completed
* [ ] Python SDK execution successful

---

## GitHub Validation

* [ ] Repository publicly accessible
* [ ] Screenshots display correctly
* [ ] Markdown renders correctly
* [ ] Code blocks render correctly
* [ ] Links function correctly

---

# Author

## James Banday

Cloud Engineering | Cybersecurity | AI | Platform Engineering

### GitHub

https://github.com/jbanday808

### LinkedIn

https://www.linkedin.com/in/james-allen-morta-banday-62a391128/


---

## Project Status

```text
Status: Complete
Version: 1.0
Platform: Microsoft Foundry IQ
Cloud Provider: Microsoft Azure
Language: Python
Repository: foundry-iq-agent
```


