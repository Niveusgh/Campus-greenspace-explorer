# Purpose: Handles HTTP requests (like when user clicks "submit" on your webpage)
from flask import Blueprint, jsonify, request
from services.custom_tree_service import CustomTreeService

tree_routes = Blueprint('trees', __name__)
custom_service = CustomTreeService()

@tree_routes.route('/api/trees/custom', methods=['POST'])
def add_custom_tree():
    # 1. Gets data from webpage form
    tree_data = request.json  # Example: {"species": "Oak", "location": "Near Library"}
    
    # 2. Passes data to service
    try:
        new_tree = custom_service.add_tree(tree_data)
        return jsonify({"message": "Tree added successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
