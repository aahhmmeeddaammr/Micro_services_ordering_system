from flask import request, jsonify
from ..services.services import  get_all_orders

def register_routes(app):
    @app.route("/api/orders", methods=["GET"])
    def get_all_orders_route():
        result = get_all_orders()
        return jsonify(result), 200 if result["success"] else 404
    