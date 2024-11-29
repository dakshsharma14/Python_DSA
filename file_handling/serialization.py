import json

data = {
    "name": "John Dough",
    "age": 34,
    "city": "new york"
}

json_data = json.dumps(data)
# converted this to a string
print(json_data)

