from flask import Flask, render_template
from flask import send_from_directory
import os

app = Flask(__name__)

# Add this line for development
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/wellness')
def wellness():
    return render_template('wellness.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Add this route to app.py for testing
@app.route('/test-logo')
def test_logo():
    try:
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
                                 'logo.png')
    except Exception as e:
        return f"Error: {str(e)}", 404
    
if __name__ == '__main__':
    app.run(debug=True)