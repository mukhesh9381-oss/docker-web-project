
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My First DevOps Project!</h1>
    <p>My Python web application is running inside Docker.</p>
    <p>Docker + Python + Flask = Success!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
