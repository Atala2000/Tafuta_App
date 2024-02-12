#!/usr/bin/env python3
"""Database storage engine"""
from datetime import datetime
from . import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(20))


class Item_found(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    item_description = db.Column(db.String(100))
    item_location = db.Column(db.String(100))
    item_date = db.Column(db.DateTime, default=datetime.now)
    item_status = db.Column(db.String(100))
    item_user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    user = db.relationship("User", backref="item_found")


class Item_retrieved(db.Model):
    date_retrieved = db.Column(db.DateTime, default=datetime.now)
    item_id = db.Column(db.Integer, db.ForeignKey("item_found.id"))
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    finder_id = db.Column(db.Integer, db.ForeignKey("user.id"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
