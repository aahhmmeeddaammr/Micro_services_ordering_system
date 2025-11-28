from ..utils.db_connection import execute_query, execute_update

class Order:
    """Order model for interacting with orders and order_items tables"""
    
    @staticmethod
    def create_order(customer_id, total_amount):
        """Create a new order"""
        query = "INSERT INTO orders (customer_id, total_amount) VALUES (%s, %s)"
        return execute_update(query, (customer_id, total_amount))
    
    @staticmethod
    def get_order_by_id(order_id):
        """Get order by ID"""
        query = "SELECT * FROM orders WHERE order_id = %s"
        result = execute_query(query, (order_id,))
        return result[0] if result else None
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        """Get all orders for a customer"""
        query = "SELECT * FROM orders WHERE customer_id = %s ORDER BY created_at DESC"
        return execute_query(query, (customer_id,))
    
    @staticmethod
    def get_all_orders():
        """Get all orders"""
        query = "SELECT * FROM orders ORDER BY created_at DESC"
        return execute_query(query)
    
    @staticmethod
    def add_order_item(order_id, product_id, quantity, price):
        """Add item to order"""
        query = "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)"
        return execute_update(query, (order_id, product_id, quantity, price))
    
    @staticmethod
    def get_order_items(order_id):
        """Get all items for an order"""
        query = "SELECT * FROM order_items WHERE order_id = %s"
        return execute_query(query, (order_id,))
    
    @staticmethod
    def update_order_total(order_id, total_amount):
        """Update order total amount"""
        query = "UPDATE orders SET total_amount = %s WHERE order_id = %s"
        return execute_update(query, (total_amount, order_id))
