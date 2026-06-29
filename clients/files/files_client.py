from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class CreateFileRequestDict(TypedDict):
    """Описание структуры запроса на создание файла"""
    filename: str
    directory: str
    upload_file: str

class FilesClient(APIClient):
    """Клиент для отправки файлов (/api/v1/files)"""
    def get_file_by_id(self, file_id: str) -> Response:
        """Метод на получение файла по его идентификатору"""
        return self.get(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestDict) -> Response:
        """Метод создания файла на сервере"""
        return self.post(
            f"/api/v1/files",
            data=request,
            files={"upload_file": open(request["upload_file"], "rb")}
        )

    def delete_file_by_id(self, file_id: str) -> Response:
        return self.delete(f"/api/v1/files/{file_id}")

def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))