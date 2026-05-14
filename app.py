from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD pipeline works 🚀🔥"

@app.route("/stress")
def stress():
    start = time.time()

    while time.time() - start < 20:
        x = 99999 * 99999

    return "CPU stress completed 🔥"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)