import socket
from http.server import HTTPServer
from queue import Queue
from socketserver import ThreadingMixIn
from threading import Thread


class ThreadPoolMixIn(ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
    last_time = 0
    reqs = {}
    thread_count = 0
    requests = Queue()

    def serve_forever(self, thread_count=10):
        self.thread_count = thread_count
        self.requests = Queue()

        for one in range(self.thread_count):
            thread = Thread(target=self.process_request_thread)
            thread.daemon = True
            thread.start()

        while True:
            self.handle_request()

    def process_request_thread(self, *args):
        while True:
            ThreadingMixIn.process_request_thread(self, *self.requests.get())

    def handle_request(self):
        try:
            request, client_address = self.get_request()
        except socket.error:
            return

        if self.verify_request(request, client_address):
            self.requests.put((request, client_address))
