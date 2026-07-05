from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus

from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response


def test_create_user():
    public_users_client = get_public_users_client() #делаем клиент, тело запроса, с помощью клиента кидаем запрос на создания пользователя и получаем ответ

    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text) #мы валидируем ответ тут со схемой, но если попадется "1", то это будет тип int поэтому дальше есть вторая валидация

    #assert response.status_code == HTTPStatus.OK, "Некорректный статус код ответа" #проверяем статус код и дальше проверяем все ли поля те же самые что ушли
    assert_status_code(response.status_code, HTTPStatus.OK) # эквивалент вышестоящей строчки кода

    # assert response_data.user.email == request.email, "Некорректный email пользователя"
    # assert response_data.user.first_name == request.first_name, "Некорректный first_name пользователя"
    # assert response_data.user.last_name == request.last_name, "Некорректный last_name пользователя"
    # assert response_data.user.middle_name == request.middle_name, "Некорректный middle_name пользователя"

    assert_create_user_response(request, response_data) #аналог вышестоящих строк, проверяем что значения, которые отправляли вернулись те же самые

    validate_json_schema(response.json(), response_data.model_json_schema()) #response_data.model_json_schema() генерирует схему на основе CreateUserResponseSchema и проверяет по ней ответ
    #можно сказать что в строке выше мы проверяем уже структуру и типы значений, а сами значения проверяем на 25-ой

    

