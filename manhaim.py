import requests

headers = {
    'Authorization': 'Basic aDNod2dtNDQ0NWtqenB0XXXXXXXXXXXXX=',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'grant_type': 'client_credentials',
}

response = requests.post('https://api.manheim.com/oauth2/token.oauth2', headers=headers, data=data)
print(response.content)