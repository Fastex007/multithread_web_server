import json
from http import HTTPStatus

from core.urls import router


class RequestPrepare:
    """Подготавливает ответ."""

    def __init__(self, path):
        self.__path = path

    @staticmethod
    def prepare_path(path: str) -> str:
        path = path.lower()
        if not path.endswith("/"):
            path = f"{path}/"
        return path

    def response_prepare(self) -> tuple:
        path = self.prepare_path(self.__path)
        method = router.get(path)

        if not method:
            return self.handle_error(HTTPStatus.NOT_FOUND, "Страница не найдена.")

        try:
            result = method()
        except Exception as exc:
            return self.handle_error(HTTPStatus.SERVICE_UNAVAILABLE, f"Сервис недоступен, ({exc}).")

        return HTTPStatus.OK, json.dumps(result, ensure_ascii=False)

    def handle_error(self, status_code: int = None, message: str = None) -> tuple:
        PREFIX = "ERROR"
        if not status_code:
            status_code = HTTPStatus.SERVICE_UNAVAILABLE
        return status_code, json.dumps({f"{PREFIX} {status_code}": message}, ensure_ascii=False)