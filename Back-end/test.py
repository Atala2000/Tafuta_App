#!/usr/bin/env python3
"""
Testing Flask works
"""
from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route("/users", strict_slashes=False)
def hello_hbnb():
    """Print Hello HBNB!"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
