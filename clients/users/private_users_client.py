from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient

from clients.private_http_builder import get_private_http_client
from clients.private_http_builder import AuthenticationUserDict
class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление пользовател
    """
    email: str | None
    password: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def get_get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по его uuid
        :param user_id: id пользователя
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def get_update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Метод частичного обновления данных пользователя по его uuid
        :param user_id: id пользователя
        :param request: словарь с данными для обновления
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по его uuid
        :param user_id: id пользователя
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))


