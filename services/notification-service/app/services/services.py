from ..models import Notification


def get_all_notifications():
    """Get all notifications"""
    notifications = Notification.get_all_notifications()
    return {
        "success": True,
        "notifications": [
            {
                "notification_id": n["notification_id"],
                "order_id": n["order_id"],
                "customer_id": n["customer_id"],
                "notification_type": n["notification_type"],
                "message": n["message"],
                "sent_at": str(n["sent_at"])
            }
            for n in notifications
        ] if notifications else []
    }
