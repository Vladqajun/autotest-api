"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""
import uuid

from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"

class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=100)
    min_score: int = Field(alias="minScore", default=10)
    description: str = "description"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")


course_default_model = CourseSchema(
    id="course_id",
    title="title",
    maxScore=100,
    minScore=10,
    description="description",
    previewFile=FileSchema(
        id="preview_file_id",
        filename="preview_file",
        directory="directory",
        url="https://example.com/"
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="created_by_user_id",
        email="user@mail.com",
        firstName="Petya",
        lastName="Stepanov",
        middleName="Galya"
    )
)
print("course_default_model: ", course_default_model)

course_dict = {
    "id": "course_id",
    "title": "title",
    "maxScore": 100,
    "minScore": 10,
    "description": "description",
    "previewFile": {
        "id": "preview_file_id",
        "filename": "user@mail.com",
        "directory": "directory",
        "url": "https://example.com/"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
    "id": "created_by_user_id",
    "email": "user@mail.com",
    "lastName": "Petya",
    "firstName": "Stepanov",
    "middleName": "Galya"
    }
}

course_dict_model = CourseSchema(**course_dict)
print("course_dict_model: ", course_dict_model)

course_json = """
{
    "id": "course_id",
    "title": "title",
    "maxScore": 100,
    "minScore": 10,
    "description": "description",
    "previewFile": {
        "id": "preview_file_id",
        "filename": "user@mail.com",
        "directory": "directory",
        "url": "https://example.com/"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
    "id": "created_by_user_id",
    "email": "user@mail.com",
    "lastName": "Petya",
    "firstName": "Stepanov",
    "middleName": "Galya"
    }
}
"""
course_json_module = CourseSchema.model_validate_json(course_json)
print("course_json_module: ", course_json_module)
print(course_json_module.model_dump(by_alias=True))
print(course_json_module.model_dump_json(by_alias=True))


try:
    user = UserSchema(
        id="created_by_user_id",
        email="user@com",
        firstName="Petya",
        lastName="Stepanov",
        middleName="Galya"
    )
    print(user.get_username(), user.username)
except ValidationError as error:
    print(error)
    print(error.errors())
