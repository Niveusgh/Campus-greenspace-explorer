import pandas as pd
import sqlite3

def import_csv():
    # Read CSV
    df = pd.read_csv('data/UKTrees.csv')
    
    # Clean column names
    df.columns = [
        'common_name',
        'latin_name',
        'dbh',
        'latitude',
        'longitude',
        'tree_id'
    ]
    
    # Handle null values
    df = df.fillna({
        'common_name': 'Unknown',
        'latin_name': 'Species Unknown',
        'dbh': 0.0,
        'latitude': 0.0,
        'longitude': 0.0,
        'tree_id': df['tree_id'].max() + 1  # Generate new ID if missing
    })
    
    # Data validation
    print("Checking for nulls before import:")
    print(df.isnull().sum())
    
    # Connect to database
    conn = sqlite3.connect('instance/UKTrees.db')
    cursor = conn.cursor()
    
    # Create table with NOT NULL constraints where needed
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trees (
        tree_id INTEGER PRIMARY KEY NOT NULL,
        common_name TEXT NOT NULL DEFAULT 'Unknown',
        latin_name TEXT NOT NULL DEFAULT 'Species Unknown',
        dbh REAL NOT NULL DEFAULT 0.0,
        latitude REAL NOT NULL DEFAULT 0.0,
        longitude REAL NOT NULL DEFAULT 0.0
    )
    """)
    
    # Import data
    df.to_sql('trees', conn, if_exists='replace', index=False)
    
    # Verify import
    cursor.execute("SELECT COUNT(*) FROM trees")
    count = cursor.fetchone()[0]
    print(f"\nImported {count} trees")
    
    # Check for any remaining null values in database
    cursor.execute("""
    SELECT 
        COUNT(*) - COUNT(tree_id) as tree_id_nulls,
        COUNT(*) - COUNT(common_name) as common_name_nulls,
        COUNT(*) - COUNT(latin_name) as latin_name_nulls,
        COUNT(*) - COUNT(dbh) as dbh_nulls,
        COUNT(*) - COUNT(latitude) as latitude_nulls,
        COUNT(*) - COUNT(longitude) as longitude_nulls
    FROM trees
    """)
    print("\nNull check in database:")
    null_counts = cursor.fetchone()
    print(f"tree_id nulls: {null_counts[0]}")
    print(f"common_name nulls: {null_counts[1]}")
    print(f"latin_name nulls: {null_counts[2]}")
    print(f"dbh nulls: {null_counts[3]}")
    print(f"latitude nulls: {null_counts[4]}")
    print(f"longitude nulls: {null_counts[5]}")
    
    conn.close()

if __name__ == '__main__':
    import_csv()