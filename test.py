from httpx import head

from files import files_client as fc
import httpx

from files.files_client import CreateFileRequestDict


login_payload = {
    "email": "user@example.com",
    "password": "string",
}
print("1 запрос")
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

client = fc.FilesClient(
    client=httpx.Client(
        base_url="http://localhost:8000",
    )
)
request_data: CreateFileRequestDict = {
    "filename": "my_test_file.jpg",
    "directory": "courses/photos",
    "upload_file": "C:/Users/EpticExp/Desktop/test3.jpg"
}


response = client.create_file(request_data)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

