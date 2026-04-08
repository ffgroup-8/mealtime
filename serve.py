import os, http.server, socketserver

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 3000
handler = http.server.SimpleHTTPRequestHandler
handler.log_message = lambda *a: None  # silence access logs

with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()
