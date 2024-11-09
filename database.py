# database.py
import sqlite3
import os

def create_db():
    # Make instance directory if it doesn't exist
    if not os.path.exists('instance'):
        os.makedirs('instance')
    
    # Connect to database (creates it if it doesn't exist)
    conn = sqlite3.connect('instance/UKTrees.db')
    c = conn.cursor()
    
    # Create tables
    c.executescript('''
    CREATE TABLE IF NOT EXISTS trees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        species_name TEXT NOT NULL,
        common_name TEXT,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL,
        height_meters REAL,
        diameter_cm REAL,
        plant_date DATE,
        health_status TEXT CHECK(health_status IN ('Good', 'Fair', 'Poor', 'Critical')),
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS species (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        scientific_name TEXT UNIQUE NOT NULL,
        common_name TEXT,
        native_to_uk BOOLEAN,
        description TEXT
    );

    CREATE TABLE IF NOT EXISTS maintenance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tree_id INTEGER,
        maintenance_date DATE NOT NULL,
        maintenance_type TEXT NOT NULL,
        notes TEXT,
        FOREIGN KEY (tree_id) REFERENCES trees(id)
    );

    CREATE INDEX IF NOT EXISTS idx_trees_location ON trees(latitude, longitude);
    CREATE INDEX IF NOT EXISTS idx_trees_species ON trees(species_name);
    CREATE INDEX IF NOT EXISTS idx_maintenance_tree ON maintenance(tree_id);
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()