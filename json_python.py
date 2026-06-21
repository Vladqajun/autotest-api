import json

data = {
    "name": "Мария",
    "age": 25,
    "is_student": True
}

json_string = json.dumps(data, indent=4)  # Преобразуем Python-объект в JSON-строку
print(json_string)
