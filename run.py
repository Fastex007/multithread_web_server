from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer

from config import Parameters
from core.middleware import RequestPrepare
from core.mixin import ThreadPoolMixIn
from core.service_monitoring import ServiceMonitoring, duration_monitoring


class RequestHandler(BaseHTTPRequestHandler):
    """Обрабатывает запросы."""

    @duration_monitoring
    def send_error(self, code, message=None, explain=None) -> None:
        status_code, response = RequestPrepare(self.path).handle_error(message=message)
        self.response(status_code, response, message)

    @duration_monitoring
    def do_GET(self) -> None:
        status_code, response = RequestPrepare(self.path).response_prepare()
        self.response(status_code, response)

    def response(self, status_code, response, message=None) -> None:
        config = Parameters.config
        self.send_response(status_code)
        self.send_header('Content-Type', config.get_env(var_name="CONTENT_TYPE", default="application/json"))
        self.end_headers()
        self.wfile.write(response.encode(encoding=config.get_env(var_name="ENCODING", default="utf_8")))
        Parameters.logger.info(f"Запрос: {self.command}, {self.path}. "
                               f"Ответ: {status_code} {response if status_code != HTTPStatus.OK else message}")


class ServerThreading(ThreadPoolMixIn):
    pass


def run_server(service_address: str = 'localhost', service_port=80) -> None:
    server = ServerThreading(
        server_address=(service_address, service_port),
        RequestHandlerClass=RequestHandler,
    )
    Parameters.logger.info(f"Запущен сервер http://{service_address}:{service_port}")
    server.serve_forever(thread_count=int(Parameters.config.get_env("THREAD_COUNT")))


if __name__ == '__main__':
    Parameters.monitoring = ServiceMonitoring()
    run_server(
        service_address=Parameters.config.get_env("SERVICE_ADDRESS"),
        service_port=int(Parameters.config.get_env("SERVICE_PORT")),
    )
