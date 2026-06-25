import httpx

print("Результат выполнения 1-го запроса:")
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)
print(response.json(), end="\n\n")

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

print("Результат выполнения 2-го запроса:")
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)
print(response.json(), end="\n\n")

print("Результат выполнения 3-го запроса:")
data = {"username": "test_user", "password": "123456"}

response = httpx.post("https://httpbin.org/post", data=data)

print(response.status_code)
print(response.json(), end="\n\n")

print("Результат выполнения 4-го запроса:")
headers = {"Authorization": "Bearer my_secret_test_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.request.headers)
print(response.json(), end="\n\n")

print("Результат выполнения 5-го запроса:")
params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)
print(response.json(), end="\n\n")

print("Результат выполнения 6-го запроса:")
files = {"file": ("example.txt", open("example", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json(), end="\n\n")

print("Результат выполнения 7-го запроса:")
with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())
print(response2.json())

print("Результат выполнения 8-го запроса:")
client = httpx.Client(headers={"Authorization": "Bearer my_secret_test_token"}) #теперь заголовки будут автоматически вставляться
response = client.get("https://httpbin.org/get")
print(response.json(), end="\n\n")

print("Результат выполнения 9-го запроса:")
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalir-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

print("Результат выполнения 10-го запроса:")
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Зпрос привысил лимит времени")