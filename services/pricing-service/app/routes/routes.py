from flask import request, jsonify
from ..services.services import (
     
     get_all_pricing_rules
     )

def register_routes(app):
 
    @app.route("/api/pricing/rules", methods=["GET"])
    def get_pricing_rules_route():
        result = get_all_pricing_rules()
        return jsonify(result), 200 if result["success"] else 404
