# services/custom_tree_service.py
from .database import Database
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class CustomTreeService:
    def __init__(self):
        self.db = Database()

    def add_tree(self, tree_data: Dict) -> Tuple[bool, str, Optional[int]]:
        """Add a new tree from user input"""
        try:
            query = """
            INSERT INTO trees (
                common_name, latin_name, dbh,
                latitude, longitude
            ) VALUES (?, ?, ?, ?, ?)
            """
            params = (
                tree_data.get('common_name', 'Unknown'),
                tree_data.get('latin_name', 'Species Unknown'),
                float(tree_data.get('dbh', 0)),
                float(tree_data['latitude']),  # Required
                float(tree_data['longitude'])  # Required
            )
            
            tree_id = self.db.execute_write(query, params)
            return True, "Tree added successfully", tree_id
        except KeyError:
            return False, "Missing required location data", None
        except ValueError:
            return False, "Invalid numeric values provided", None
        except Exception as e:
            return False, f"Error adding tree: {str(e)}", None

    def update_tree(self, tree_id: int, tree_data: Dict) -> Tuple[bool, str]:
        """Update existing tree details"""
        try:
            # Verify tree exists
            existing = self.db.execute_query(
                "SELECT * FROM trees WHERE tree_id = ?", 
                (tree_id,)
            )
            if not existing:
                return False, "Tree not found"

            query = """
            UPDATE trees 
            SET common_name = ?, 
                latin_name = ?,
                dbh = ?,
                latitude = ?,
                longitude = ?
            WHERE tree_id = ?
            """
            params = (
                tree_data.get('common_name', existing[0][1]),
                tree_data.get('latin_name', existing[0][2]),
                float(tree_data.get('dbh', existing[0][3])),
                float(tree_data.get('latitude', existing[0][4])),
                float(tree_data.get('longitude', existing[0][5])),
                tree_id
            )
            
            self.db.execute_write(query, params)
            return True, "Tree updated successfully"
        except Exception as e:
            return False, f"Error updating tree: {str(e)}"

    def delete_tree(self, tree_id: int) -> Tuple[bool, str]:
        """Delete a tree record"""
        try:
            # Check if tree exists
            existing = self.db.execute_query(
                "SELECT * FROM trees WHERE tree_id = ?", 
                (tree_id,)
            )
            if not existing:
                return False, "Tree not found"

            query = "DELETE FROM trees WHERE tree_id = ?"
            self.db.execute_write(query, (tree_id,))
            return True, "Tree deleted successfully"
        except Exception as e:
            return False, f"Error deleting tree: {str(e)}"

    def get_nearby_trees(self, lat: float, lng: float, radius_km: float = 0.5) -> List[Dict]:
        """Find trees within specified radius"""
        trees = self.db.get_trees_in_radius(lat, lng, radius_km)
        return [self._format_tree(tree) for tree in trees]

    def validate_tree_data(self, tree_data: Dict) -> Tuple[bool, str]:
        """Validate tree data before adding/updating"""
        required_fields = ['latitude', 'longitude']
        
        # Check required fields
        for field in required_fields:
            if field not in tree_data:
                return False, f"Missing required field: {field}"
        
        try:
            # Validate coordinates
            lat = float(tree_data['latitude'])
            lng = float(tree_data['longitude'])
            if not (-90 <= lat <= 90 and -180 <= lng <= 180):
                return False, "Invalid coordinates"

            # Validate DBH if provided
            if 'dbh' in tree_data:
                dbh = float(tree_data['dbh'])
                if dbh < 0:
                    return False, "DBH cannot be negative"
                
            return True, "Data valid"
        except ValueError:
            return False, "Invalid numeric values"

    def _format_tree(self, tree_tuple: tuple) -> Dict:
        """Format tree data for output"""
        return {
            'tree_id': tree_tuple[0],
            'common_name': tree_tuple[1],
            'latin_name': tree_tuple[2],
            'dbh': tree_tuple[3],
            'latitude': tree_tuple[4],
            'longitude': tree_tuple[5],
            'distance': tree_tuple[6] if len(tree_tuple) > 6 else None
        }