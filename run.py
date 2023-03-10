from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

from config import Config, Parameters
from core.middleware import RequestPrepare
from core.service_monitoring import ServiceMonitoring, duration_monitoring


class RequestHandler(BaseHTTPRequestHandler):
    """Обрабатывает запросы."""

    @duration_monitoring
    def send_error(self, code, message=None, explain=None) -> None:
        status_code, response = RequestPrepare(self.path).handle_error()
        self.response(status_code, response)

    @duration_monitoring
    def do_GET(self) -> None:
        status_code, response = RequestPrepare(self.path).response_prepare()
        self.response(status_code, response)

    def response(self, status_code, response) -> None:
        config = Parameters.config
        self.send_response(status_code)
        self.send_header('Content-Type', config.get_env(var_name="CONTENT_TYPE", default="application/json"))
        self.end_headers()
        self.wfile.write(response.encode(encoding=config.get_env(var_name="ENCODING", default="utf_8")))


class ServerThreading(ThreadingMixIn, HTTPServer):
    pass


def run_server(service_address: str = 'localhost', service_port=80) -> None:
    server = ServerThreading((service_address, service_port), RequestHandler)
    print(f"Запущен сервер http://{service_address}:{service_port}")
    server.serve_forever()


if __name__ == '__main__':
    Parameters.config = Config()
    Parameters.monitoring = ServiceMonitoring()
    run_server(
        service_address=Parameters.config.get_env("SERVICE_ADDRESS"),
        service_port=int(Parameters.config.get_env("SERVICE_PORT")),
    )
