import requests

question_data = []

parameters = {
    "amount": 10,
    "type": "boolean"
}

"""this function fetchs a data"""
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  # handles any exceptions that may occur during fetching a data
data = response.json()
print(data["results"])
for item in data["results"]:
    question_data.append(item)
# question.append(data["results"])
