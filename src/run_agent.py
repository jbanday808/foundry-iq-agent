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