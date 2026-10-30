
from http.server import HTTPServer, BaseHTTPRequestHandler

class App(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
        <body>
        <h1>Welcome to My Website</h1>
        <h2>OWASP ZAP Security Testing</h2>
        </body>
        </html>
        """

        self.wfile.write(html.encode())

server = HTTPServer(("0.0.0.0", 8000), App)

print("Server Started")
server.serve_forever()
