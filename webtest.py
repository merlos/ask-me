import requests

BASE = "http://localhost:5000"

print("GET /")
response = requests.get(BASE + '/')


payload = dict(question='Who is Juan?')
print (f"POST /api/answers {payload}")
print ("Response:")
response = requests.post(BASE + "/api/answers", data=payload)
print(response.json())