import requests
import json

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiMTlhMjc2ZC03NGVmLTQ2MjgtYjcxZi01MWNhODE1OTQyNjQiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwianRpIjoiN2IyZGZkNDctMjg2Mi00MjhkLWFkODUtZGMyMTc4NTNiMGFmIiwiaWF0IjoxNzc5OTIwMzA0fQ.v0yb_QvnbaQ13tUpXje4a6AEPHhYzQJMR3cb9wjUTzc"
execution_id = "288"
api_url = f"https://n8n-n8n.0xxtfo.easypanel.host/api/v1/executions/{execution_id}"

headers = {
    "X-N8N-API-KEY": api_key
}

response = requests.get(api_url, headers=headers)
print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    # Print the error or details of execution
    print(json.dumps(data, indent=2))
else:
    print(response.text)
