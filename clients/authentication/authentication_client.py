from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class LoginRequestDict(TypedDict):
    """
    Содержит информацию о необходимых полях для логина
    """
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    """
    Содержит информацию о необходимых полях для refresh токена
    """
    refreshToken: str

class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.
        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)


    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации
        :param request: Словарь с refreshToken
        :return: Возвращает ответ от сервера в виде объекта типа httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)
