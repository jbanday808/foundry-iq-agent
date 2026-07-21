# Python Script Walkthrough

## Full Script

```python
# Before running this script, install the required packages:
# pip install azure-ai-projects>=2.1.0 azure-identity

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


# Azure AI Foundry project endpoint
endpoint = "https://foundry-iq-jbanday.services.ai.azure.com/api/projects/proj-default"


# Create the Azure AI Project client
project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)


# Foundry IQ agent configuration
my_agent = "enterprise-knowledge-agent"
my_version = "5"


# Create OpenAI client from Azure AI Project
openai_client = project_client.get_openai_client()


# Validation questions
questions = [
    "What is the service name of the Azure AI Search resource?",
    "What resource group was used?",
    "What region was selected?",
    "What is the name of the agent?",
    "Summarize the uploaded document.",
]


# Run validation tests
for question in questions:
    response = openai_client.responses.create(
        input=[
            {
                "role": "user",
                "content": question,
            }
        ],
        extra_body={
            "agent_reference": {
                "name": my_agent,
                "version": my_version,
                "type": "agent_reference",
            }
        },
    )

    print("\n----------------------------------------")
    print(f"Question: {question}")
    print(f"Response output: {response.output_text}")
```

---

## Script Breakdown

### Package Installation

```python
# pip install azure-ai-projects>=2.1.0 azure-identity
```

**Explanation:**

Installs the software libraries needed for the script to communicate with Microsoft Foundry IQ and securely access Azure resources.

---

### Import Required Libraries

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
```

**Explanation:**

Imports the Azure tools used to securely sign in and connect to the Microsoft Foundry IQ project.

---

### Foundry IQ Project Endpoint

```python
endpoint = "https://foundry-iq-jbanday.services.ai.azure.com/api/projects/proj-default"
```

**Explanation:**

Specifies the Microsoft Foundry IQ project that the script will connect to.

---

### Create Azure AI Project Client

```python
project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)
```

**Explanation:**

Creates a secure connection to the Foundry IQ project using the Azure account currently signed in on the computer.

---

### Agent Configuration

```python
my_agent = "enterprise-knowledge-agent"
my_version = "5"
```

**Explanation:**

Identifies which AI agent and version the script should use when asking questions.

---

### Create OpenAI Client

```python
openai_client = project_client.get_openai_client()
```

**Explanation:**

Creates the communication channel used to send questions to the AI agent and receive responses.

---

### Validation Questions

```python
questions = [
    "What is the service name of the Azure AI Search resource?",
    "What resource group was used?",
    "What region was selected?",
    "What is the name of the agent?",
    "Summarize the uploaded document.",
]
```

**Explanation:**

Creates a list of test questions used to verify that the AI agent is working correctly and can retrieve information from the connected knowledge base.

---

### Run Validation Tests

```python
for question in questions:
```

**Explanation:**

Starts a loop that sends each question to the AI agent one at a time.

---

### Submit the Question

```python
response = openai_client.responses.create(
```

**Explanation:**

Submits a question to the AI agent and waits for a response.

---

### User Input

```python
input=[
    {
        "role": "user",
        "content": question,
    }
]
```

**Explanation:**

Formats the question as if it were entered by a user in the Foundry IQ chat window.

---

### Agent Reference

```python
extra_body={
    "agent_reference": {
        "name": my_agent,
        "version": my_version,
        "type": "agent_reference",
    }
}
```

**Explanation:**

Tells Foundry IQ exactly which AI agent should answer the question.

---

### Display Results

```python
print("\n----------------------------------------")
print(f"Question: {question}")
print(f"Response output: {response.output_text}")
```

**Explanation:**

Displays the question and the AI agent's answer on the screen so the results can be reviewed.

---

## Expected Output

```text
----------------------------------------
Question: What is the service name of the Azure AI Search resource?

Response output:
caremedix-search

----------------------------------------
Question: What resource group was used?

Response output:
Sentinel-RG

----------------------------------------
Question: What region was selected?

Response output:
East US
```

---

## Summary

This script connects to Microsoft Foundry IQ, sends validation questions to the **enterprise-knowledge-agent**, retrieves answers from the connected knowledge base, and displays the results to verify that the AI agent is functioning correctly.
