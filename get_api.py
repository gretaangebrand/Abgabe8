import requests

## Get all persons
# Define the URL of the API
url = "http://127.0.0.1:5000/person/"

# Send a GET request to the API with the name as a query parameter
response = requests.get(url)

# Print the response from the server
print(response.text)


## Get a person by name
# Define the URL of the API

url = "http://127.0.0.1:5000/person/TestName"

# Send a GET request to the API with the name as a query parameter
response = requests.get(url)

# Print the response from the server
print(response.text)
