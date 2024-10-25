# config.py

class Config:
    # Database settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///campus_trees.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max file size 16MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    
    # Map default center (UK campus)
    DEFAULT_LAT = 38.0406
    DEFAULT_LNG = -84.5037
    DEFAULT_ZOOM = 15

class DevelopmentConfig(Config):
    DEBUG = True
    # Development-specific settings
    TEMPLATES_AUTO_RELOAD = True

class ProductionConfig(Config):
    DEBUG = False
    # Production-specific settings
    # Could add different database URL, etc.

# app.py - How to use it
from flask import Flask
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Now you can use settings anywhere:
@app.route('/map')
def map():
    return render_template('map.html',
                         default_lat=app.config['DEFAULT_LAT'],
                         default_lng=app.config['DEFAULT_LNG'],
                         default_zoom=app.config['DEFAULT_ZOOM'])