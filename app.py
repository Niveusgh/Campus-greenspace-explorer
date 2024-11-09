from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
from datetime import datetime
import os
from services.database import Database
from services.uk_tree_service import UKTreeService

app = Flask(__name__)
CORS(app)

# Development configuration
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Campus data dictionary - main feature content
CAMPUS_DATA = {
    'map_layers': [
        {'id': 'buildings', 'name': 'Buildings'},
        {'id': 'spaces', 'name': 'Green Spaces'},
        {'id': 'paths', 'name': 'Paths'}
    ],
    'location_info': {
        'WT Young Library Lawn': {
            'description': 'An open space perfect for sunbathing and outdoor studying.',
            'features': ['Open Grass Area', 'Study Spots', 'WiFi Access', 'Natural Shade']
        },
        'President Garden': {
            'description': 'A serene garden featuring a beautiful lily pond and various native plants.',
            'features': ['Lily Pond', 'Native Plants', 'Benches', 'Shade Trees']
        }
    }
}

# Register blueprints
from routes.tree_routes import tree_routes
app.register_blueprint(tree_routes)

# Initialize database
@app.cli.command('init-db')
def init_db_command():
    """Clear existing data and create new tables."""
    db = Database()
    db.get_connection()
    print('Initialized the database.')

@app.cli.command('import-trees')
def import_trees_command():
    """Import trees from CSV."""
    uk_service = UKTreeService()
    csv_path = os.path.join('data', 'UKTrees.csv')
    success, message = uk_service.import_uk_trees(csv_path)
    print(message)

# Main routes
@app.route('/')
def index():
    return render_template('index.html',
                         map_layers=CAMPUS_DATA['map_layers'],
                         location_info=CAMPUS_DATA['location_info'])

@app.route('/wellness')
def wellness():
    return render_template('wellness.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Template context processor for global variables
@app.context_processor
def utility_processor():
    return {'current_year': datetime.now().year}

if __name__ == '__main__':
    app.run(debug=True)