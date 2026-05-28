import requests
import json

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiMTlhMjc2ZC03NGVmLTQ2MjgtYjcxZi01MWNhODE1OTQyNjQiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwianRpIjoiN2IyZGZkNDctMjg2Mi00MjhkLWFkODUtZGMyMTc4NTNiMGFmIiwiaWF0IjoxNzc5OTIwMzA0fQ.v0yb_QvnbaQ13tUpXje4a6AEPHhYzQJMR3cb9wjUTzc"

headers = {
    "X-N8N-API-KEY": api_key
}

# Fetch the specific workflow for Finca Los Pinos
response1 = requests.get("https://n8n-n8n.0xxtfo.easypanel.host/api/v1/workflows/inXBN3rrIUveuErK", headers=headers)
# Fetch the Chatbot1 workflow
response2 = requests.get("https://n8n-n8n.0xxtfo.easypanel.host/api/v1/workflows/nNagSgCL1HuxATPm", headers=headers)

if response1.status_code == 200:
    wf1 = response1.json()
    print("Workflow Finca Los Pinos:")
    print(f"  ID: {wf1.get('id')}")
    print(f"  Name: {wf1.get('name')}")
    print(f"  Active: {wf1.get('active')}")
else:
    print("Error fetching Finca Los Pinos workflow:", response1.status_code)

if response2.status_code == 200:
    wf2 = response2.json()
    print("\nWorkflow Chatbot1:")
    print(f"  ID: {wf2.get('id')}")
    print(f"  Name: {wf2.get('name')}")
    print(f"  Active: {wf2.get('active')}")
    # Print webhook paths if any
    for node in wf2.get('nodes', []):
        if node.get('type') == 'n8n-nodes-base.webhook':
            print(f"  Has Webhook Node. Path parameter: {node.get('parameters', {}).get('path')}")
else:
    print("Error fetching Chatbot1 workflow:", response2.status_code)
