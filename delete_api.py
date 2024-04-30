import requests

## Update a person
# Define the URL of the API
url = "http://127.0.0.1:5000/person/Testname2"

# Send a POST request to the API
response = requests.delete(url)

# Print the response from the server
print(response.text)