import requests

# Define the API endpoint URL
url = 'https://aimassist-server.onrender.com/api/v1/main/postRound'

# Define the array of scores to be sent in the request body
scores = [1,2,2,4,0]

# Define the request headers and payload
headers = {'Content-Type': 'application/json'}
payload = {'scores': scores}

# Send the POST request with the payload
response = requests.post(url, headers=headers, json=payload)

# Check the response status code
if response.status_code == 200:
    print('Scores posted successfully!')
else:
    print('Error posting scores:', response.content)