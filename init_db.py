# init_db.py
from services.database import Database
from services.uk_tree_service import UKTreeService
import os

def init_db():
    print("Creating instance directory if it doesn't exist...")
    if not os.path.exists('instance'):
        os.makedirs('instance')
    
    print("Initializing database...")
    db = Database()
    db.get_connection()
    print("Database initialized!")

def import_trees():
    print("Importing trees...")
    uk_service = UKTreeService()
    csv_path = os.path.join('data', 'UKTrees.csv')
    success, message = uk_service.import_uk_trees(csv_path)
    print(message)

if __name__ == '__main__':
    init_db()
    import_trees()