from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class ReqHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        self.send_response(200)
        self.send_header("Content-Type", params.get('accept')[0]) # Noncompliant
        self.end_headers()
        self.wfile.write(bytes("Hello World!", "utf-8"))

