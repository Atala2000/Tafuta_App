"""Database storage engine"""

from datetime import datetime
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Get envrionment files
load_dotenv()

app = Flask(__name__)
# Replace placeholders with your actual credentials from environment variables
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql://{os.getenv('USER_NAME')}:{os.getenv('USER_PASSWORD')}@localhost/{os.getenv('USER_DB')}"
)

# Disable track modifications to suppress warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
