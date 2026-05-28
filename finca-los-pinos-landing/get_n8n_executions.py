import requests
import json

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiMTlhMjc2ZC03NGVmLTQ2MjgtYjcxZi01MWNhODE1OTQyNjQiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwianRpIjoiN2IyZGZkNDctMjg2Mi00MjhkLWFkODUtZGMyMTc4NTNiMGFmIiwiaWF0IjoxNzc5OTIwMzA0fQ.v0yb_QvnbaQ13tUpXje4a6AEPHhYzQJMR3cb9wjUTzc"
workflow_id = "inXBN3rrIUveuErK"
api_url = f"https://n8n-n8n.0xxtfo.easypanel.host/api/v1/executions?workflowId={workflow_id}&limit=5"

headers = {
    "X-N8N-API-KEY": api_key
}

response = requests.get(api_url, headers=headers)
print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    executions = data.get("data", [])
    print(f"Found {len(executions)} recent executions:")
    for idx, exe in enumerate(executions):
        print(f"\nExecution #{idx+1}:")
        print(f"  ID: {exe.get('id')}")
        print(f"  Status: {exe.get('status')}")
        print(f"  Started: {exe.get('startedAt')}")
        print(f"  Stopped: {exe.get('stoppedAt')}")
        # Print error details if any
        error = exe.get('error')
        if error:
            print(f"  Error: {json.dumps(error, indent=2)}")
else:
    print(response.text)
