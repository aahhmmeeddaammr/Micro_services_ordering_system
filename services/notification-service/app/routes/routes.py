from flask import    jsonify
from ..services.services import  get_all_notifications

def register_routes(app):
    @app.route("/api/notifications", methods=["GET"])
    def get_all_notifications_route():
        result = get_all_notifications()
        return jsonify(result), 200 if result["success"] else 404
    
