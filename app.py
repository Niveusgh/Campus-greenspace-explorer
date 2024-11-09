from flask import Flask, render_template, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

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

# Remove /map route since map is on index

# Template context processor for global variables
@app.context_processor
def utility_processor():
    return {'current_year': datetime.now().year}

if __name__ == '__main__':
    app.run(debug=True)