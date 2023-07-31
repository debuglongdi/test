import requests
import time
import json

url = "http://127.0.0.1:6101/step1/userAgent/createWeId"

response = requests.post(url, headers={"accept": "*/*"})
if response.status_code == 200:
    data = json.loads(response.text)
    we_id = data['result']
    print("weId:", we_id)
    