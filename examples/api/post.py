import requests
import json

# Parameters
url = 'http://netcore3webapi.herokuapp.com/api/Test'
params = { 'word_id': 'music', 'lang_id': 'en-gb' } 
headers = { 'Content-Type': 'application/json' }

# Connect to the server
response = requests.post(url, headers=headers, data=json.dumps(params))

# Prepare for exceptions
try:
    response.raise_for_status()
except Exception as e:
    print(e)

# Get the result
results = response.json()

print(json.dumps(results))

