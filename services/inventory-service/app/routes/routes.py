from flask import request, jsonify
from ..services.services import (
 get_all_inventory
)

def register_routes(app):

    @app.route("/api/inventory", methods=["GET"])
    def get_all_inventory_route():
        result = get_all_inventory()
        return jsonify(result), 200 if result["success"] else 404
    