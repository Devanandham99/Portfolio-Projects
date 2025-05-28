import requests

# Zoho Books API details
access_token = 'Token'  # Replace with your access token

# Step 1: Get the Organization IDs
url = "https://samplewebsite.com"
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    organizations = response.json().get('organizations', [])
    if organizations:
        # Extract and print only the organization IDs
        print("Organization IDs:")
        for org in organizations:
            print(org['organization_id'])
    else:
        print("No organizations found.")
else:
    print(f"Failed to fetch organizations: {response.status_code}")
