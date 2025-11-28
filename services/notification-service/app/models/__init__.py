from ..utils.db_connection import execute_query, execute_update

class Notification:
    """Notification model for interacting with notification_log table"""
    
    @staticmethod
    def create_notification(order_id, customer_id, notification_type, message):
        """Create a new notification"""
        query = """
            INSERT INTO notification_log (order_id, customer_id, notification_type, message) 
            VALUES (%s, %s, %s, %s)
        """
        return execute_update(query, (order_id, customer_id, notification_type, message))
    
    @staticmethod
    def get_notification_by_id(notification_id):
        """Get notification by ID"""
        query = "SELECT * FROM notification_log WHERE notification_id = %s"
        result = execute_query(query, (notification_id,))
        return result[0] if result else None
    
    @staticmethod
    def get_notifications_by_order(order_id):
        """Get all notifications for an order"""
        query = "SELECT * FROM notification_log WHERE order_id = %s ORDER BY sent_at DESC"
        return execute_query(query, (order_id,))
    
    @staticmethod
    def get_notifications_by_customer(customer_id):
        """Get all notifications for a customer"""
        query = "SELECT * FROM notification_log WHERE customer_id = %s ORDER BY sent_at DESC"
        return execute_query(query, (customer_id,))
    
    @staticmethod
    def get_all_notifications():
        """Get all notifications"""
        query = "SELECT * FROM notification_log ORDER BY sent_at DESC"
        return execute_query(query)
