import requests
import json

# Define the URL of the API
url = "http://localhost:5000/"

# Define the data you want to send
data = {
    "name": "Frankie"
}

# Convert the data to JSON format
data_json = json.dumps(data)

# Send a POST request to the API
response = requests.put(url, data=data_json)

# Print the response from the server
print(response.text)