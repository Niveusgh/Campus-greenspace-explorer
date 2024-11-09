# services/database.py
import sqlite3
from sqlite3 import Connection, Cursor
from typing import Tuple
import pandas as pd

class Database:
    def __init__(self):
        self.db_path = 'instance/UKTrees.db'
    
    def get_connection(self) -> Connection:
        """Create and return a database connection"""
        return sqlite3.connect(self.db_path)
    
    def execute_query(self, query: str, params: Tuple = ()) -> list:
        """Execute a query and return results"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
    
    def execute_write(self, query: str, params: Tuple = ()) -> int:
        """Execute an insert/update query and return last row id"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid
    
    def bulk_insert_from_df(self, table_name: str, df: pd.DataFrame) -> None:
        """Insert data from a pandas DataFrame"""
        with self.get_connection() as conn:
            df.to_sql(table_name, conn, if_exists='append', index=False)
    
    def get_all_from_table(self, table_name: str) -> list:
        """Get all records from a table"""
        query = f"SELECT * FROM {table_name}"
        return self.execute_query(query)
    
    def get_by_id(self, table_name: str, id: int) -> tuple:
        """Get a single record by ID"""
        query = f"SELECT * FROM {table_name} WHERE tree_id = ?"
        result = self.execute_query(query, (id,))
        return result[0] if result else None

    def get_tree_count(self) -> int:
        """Get total number of trees"""
        query = "SELECT COUNT(*) FROM trees"
        result = self.execute_query(query)
        return result[0][0] if result else 0
    
    def get_trees_in_radius(self, lat: float, lng: float, radius_km: float) -> list:
        """Get trees within radius of point"""
        query = """
        SELECT *, 
            (6371 * acos(cos(radians(?)) * cos(radians(latitude)) * 
            cos(radians(longitude) - radians(?)) + sin(radians(?)) * 
            sin(radians(latitude)))) AS distance 
        FROM trees 
        HAVING distance < ? 
        ORDER BY distance
        """
        return self.execute_query(query, (lat, lng, lat, radius_km))