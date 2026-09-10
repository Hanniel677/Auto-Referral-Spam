import requests

url = "https://erp.sathyabama.ac.in/erp/api/v1.0/MasterStudent/login"

data = {
    "RegisterNumber": "YOUR_REGISTER_NUMBER",
    "Password": "YOUR_PASSWORD"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.text)

