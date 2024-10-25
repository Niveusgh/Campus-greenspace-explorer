# services/UKTreeService.py

import csv
from typing import List, Dict
from datetime import datetime

class UKTreeService:
    def __init__(self):
        self.trees_data = []
        self.csv_path = 'data/uk_trees.csv'  # Store exported file here
        self._load_trees()
    
    def _load_trees(self):
        """Load trees from exported CSV file"""
        try:
            with open(self.csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.trees_data = list(reader)
            print(f"Loaded {len(self.trees_data)} trees from CSV")
        except Exception as e:
            print(f"Error loading tree data: {e}")
            self.trees_data = []

    def get_trees_in_area(self, lat: float, lng: float, radius: float = 100) -> List[Dict]:
        """Get trees within radius of a point"""
        nearby_trees = []
        for tree in self.trees_data:
            tree_lat = float(tree.get('Latitude', 0))
            tree_lng = float(tree.get('Longitude', 0))
            if self._is_within_radius(tree_lat, tree_lng, lat, lng, radius):
                nearby_trees.append(tree)
        return nearby_trees

    def _is_within_radius(self, tree_lat: float, tree_lng: float, 
                         center_lat: float, center_lng: float, 
                         radius: float) -> bool:
        """Simple distance check"""
        from math import cos, asin, sqrt, pi
        
        def distance(lat1, lon1, lat2, lon2):
            p = pi/180
            a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
            return 12742 * asin(sqrt(a)) * 1000  # Distance in meters
            
        return distance(tree_lat, tree_lng, center_lat, center_lng) <= radius

    def get_all_trees(self) -> List[Dict]:
        """Get all trees"""
        return self.trees_data

    def get_tree_by_id(self, tree_id: str) -> Dict:
        """Get specific tree by ID"""
        for tree in self.trees_data:
            if tree.get('TreeID') == tree_id:
                return tree
        return None

    def get_species_list(self) -> List[str]:
        """Get list of unique species"""
        species = set()
        for tree in self.trees_data:
            if 'Species' in tree:
                species.add(tree['Species'])
        return sorted(list(species))