from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str
    city: str


class User(BaseModel):
    id: int
    name: str
    #address: Address
    email: str
    is_active: bool = Field(alias="isActive")

user_data = {
    "id": 1,
    "name": "Alina",
    "email": "alina@example.com",
    "isActive": True
}
user = User(**user_data)
print(user.model_dump()) #словарь
# print(user.model_dump_json()) #json
