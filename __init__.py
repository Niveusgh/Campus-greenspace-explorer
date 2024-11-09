# __init__.py (in root directory)
from routes import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)