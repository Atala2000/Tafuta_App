#!/usr/bin/env python3
"""Database storage engine"""
from datetime import datetime
from . import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(20))
    finder_id = db.relationship("Item_found", backref="user", lazy=True)


class Item_found(db.Model):
    found_item_id = db.Column(db.Integer, db.ForeignKey("item_lost.lost_item_id"), primary_key=True)
    owner_id = db.Column(db.Intger, db.ForeignKey("user.id"))
    date_found = db.Column(db.Date, default=datetime.utcnow)
    finder_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Item_lost(db.Model):
    lost_item_id = db.Column(db.Integer, primary_key=True)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
