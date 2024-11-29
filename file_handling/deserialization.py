import json

json_data = '{"name": "John Dough","age": 34,"city": "new york"}'
python_dict = json.loads(json_data)

# converted this to a string
print(python_dict)

