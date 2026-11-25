from flask import Flask
import socket
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevOps!"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/info")
def info():
    return {
        "application": "DevOps Demo App",
        "version": "1.0",
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "python_version": platform.python_version()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)