#!/usr/bin/env python3
"""
Testing Flask works
"""
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  # Allows for cross origin request


@app.route("/users", strict_slashes=False)
def hello_hbnb():
    """Print Hello HBNB!"""
    return render_template("index.html")


@app.route("/test", methods=["GET"], strict_slashes=False)
def list_users():
    return {"first_name": "John", "last_name": "Doe", "email": "Jaimie@gmail"}


@app.route("/form", methods=["POST"], strict_slashes=False)
def form():
    data = request.form
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
