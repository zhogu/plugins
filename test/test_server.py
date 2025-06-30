import sys
import http.server

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")

if len(sys.argv) > 1:
    PORT = int(sys.argv[1])
else:
    print("Usage: python custom_http_server.py [port]")
    sys.exit(1)

with http.server.HTTPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving custom HTTP on port {PORT}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")