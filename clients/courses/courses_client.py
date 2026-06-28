from typing import TypedDict

from websockets import Response

from clients.api_client import APIClient


class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str


class GetCoursesQueryRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class UpdateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses", params=query)

    def get_course(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course(self, request: GetCoursesQueryRequestDict) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return
        return self.post(f"/api/v1/courses", json=request)

    def update_course(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course(self, course_id: str) -> Response:
        """
        Метод удаления курса.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")
