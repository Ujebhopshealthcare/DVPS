from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello,You have covered 50to60 stage")

HTTPServer(('', 3000), handler).serve_forever()
