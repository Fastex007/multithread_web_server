from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

from config import Config
from core.middleware import RequestPrepare

config = None
logger = None


class RequestHandler(BaseHTTPRequestHandler):
    """Обрабатывает запросы."""

    def send_error(self, code, message=None, explain=None) -> None:
        status_code, response = RequestPrepare(self.path).handle_error()
        self.response(status_code, response)

    def do_GET(self) -> None:
        status_code, response = RequestPrepare(self.path).response_prepare()
        self.response(status_code, response)

    def response(self, status_code, response) -> None:
        self.send_response(status_code)
        self.send_header('Content-Type', config.get_env(var_name="CONTENT_TYPE", default="application/json"))
        self.end_headers()
        self.wfile.write(response.encode(encoding=config.get_env(var_name="ENCODING", default="utf_8")))


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass


def run_server(service_address: str = 'localhost', service_port=80) -> None:
    server = ThreadingSimpleServer((service_address, service_port), RequestHandler)
    print(f"Запущен сервер http://{service_address}:{service_port}")
    server.serve_forever()


if __name__ == '__main__':
    config = Config()
    run_server(
        service_address=config.get_env("SERVICE_ADDRESS"),
        service_port=int(config.get_env("SERVICE_PORT")),
    )
