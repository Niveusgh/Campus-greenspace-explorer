# Purpose: Handles HTTP requests (like when user clicks "submit" on your webpage)
# routes/tree_routes.py
from flask import Blueprint, jsonify, request
from services.uk_tree_service import UKTreeService
from services.custom_tree_service import CustomTreeService
from utils.validators import validate_tree_data

tree_routes = Blueprint('trees', __name__)
uk_service = UKTreeService()
custom_service = CustomTreeService()

@tree_routes.route('/api/trees')
def get_trees():
    """Get trees with optional filtering"""
    lat = float(request.args.get('lat', 38.0406))
    lng = float(request.args.get('lng', -84.5037))
    radius = float(request.args.get('radius', 100))
    
    # Get both UK and custom trees efficiently
    uk_trees = uk_service.get_trees_in_area(lat, lng, radius)
    custom_trees = custom_service.get_trees_in_area(lat, lng, radius)
    
    return jsonify({
        'uk_trees': uk_trees,
        'custom_trees': custom_trees
    })