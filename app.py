from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, DevOps World from a Python Flask app!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
