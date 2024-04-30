import requests
import json

## Creata a new person
# Define the URL of the API
url = "http://127.0.0.1:5000/person/"

# Define the data you want to send

data = {
    "name": "Testname2"
}

# Convert the data to JSON format
data_json = json.dumps(data)

# Send a POST request to the API
response = requests.post(url, data=data_json)

# Print the response from the server
print(response.text)