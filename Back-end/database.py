#!/usr/bin/env python3
"""Database storage engine"""
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



load_dotenv()

app = Flask(__name__)
# Replace placeholders with your actual credentials from environment variables
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{os.getenv('USER_NAME')}:{os.getenv('USER_PASSWORD')}@localhost/{os.getenv('USER_DB')}"

# Disable track modifications to suppress warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(
        db.String(128), nullable=False, unique=True, default="example@example.com"
    )
    date_joined = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"User {self.email} joined on {self.date_joined}"

class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
