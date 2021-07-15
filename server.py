#! /usr/bin/python3.9
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == '/import_list':
            self.send_header('Content-type', 'application/json')
            arr = {
                "message": "list all imports"
            }
            self.wfile.write(bytes(json.dumps(arr), "utf-8"))
        elif self.path == '/':
            self.send_header('Content-type', 'application/json')
            arr = {
                "message": "index page"
            }
            self.wfile.write(bytes(json.dumps(arr), "utf-8"))
        else: 
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            arr = {
                "message": "not foud"
            }
            self.wfile.write(bytes(json.dumps(arr), "utf-8"))


httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()