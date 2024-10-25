# for database config

# services/database.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CustomTree(db.Model):
    """Keep database models here instead of in services"""
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    # ... other fields