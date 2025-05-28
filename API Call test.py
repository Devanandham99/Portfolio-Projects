import requests

url = "https://samplewebsite/oauth/v2/token"
data = {
    "code": "APIKEY",
    "client_id": "CLIENTID",
    "client_secret": "SECRETID",
    "redirect_uri": "https://www.abcd.com/",
    "grant_type": "authorization_code"
}

response = requests.post(url, data=data)
print(response.json())
