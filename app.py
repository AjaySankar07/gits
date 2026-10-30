
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>Sample Application</title></head>
    <body>
    <h1>Welcome to Web Application</h1>
    <p>OWASP ZAP Security Testing</p>
    </body>
    </html>
    """

@app.route("/search")
def search():
    name = request.args.get("name", "")
    return "<h2>Search Result: " + name + "</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
