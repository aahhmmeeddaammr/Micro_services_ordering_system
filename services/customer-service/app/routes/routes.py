from flask import  jsonify
from ..services.services import get_customer_details

def register_routes(app):
    @app.route("/api/customers/<int:customer_id>", methods=["GET"])
    def get_customer_route(customer_id):
        result = get_customer_details(customer_id)
        return jsonify(result), 200 if result["success"] else 404
