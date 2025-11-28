from ..models import Order


def get_all_orders():
    """Get all orders"""
    try:
        orders = Order.get_all_orders()
        
        if not orders:
            return {"success": True, "orders": []}
        
        return {
            "success": True,
            "orders": [
                {
                    "order_id": order["order_id"],
                    "customer_id": order["customer_id"],
                    "total_amount": float(order["total_amount"]),
                    "created_at": str(order["created_at"])
                }
                for order in orders
            ]
        }
    
    except Exception as e:
        return {"success": False, "error": str(e)}