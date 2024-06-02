import requests

# URL of Flask-application
url = 'http://127.0.0.1:5000/predict'

# Data for send request in JSON
data = {
    "step": 305,
    "oldbalance_org": 0.000015,
    "newbalance_orig": 0.000075,
    "newbalance_dest": 0.001825,
    "diff_new_old_balance": 0.881150,
    "diff_new_old_destiny": 0.069500,
    "type_TRANSFER": 1
}

# Send POST request
response = requests.post(url, json=data)

# Print the response
print("Status Code:", response.status_code)
print("Response:", response.json())