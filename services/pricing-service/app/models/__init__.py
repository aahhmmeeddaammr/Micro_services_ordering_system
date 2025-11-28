from ..utils.db_connection import execute_query, execute_update

class PricingRule:
    """Pricing model for interacting with pricing_rules and tax_rates tables"""
    
    @staticmethod
    def get_discount(product_id, quantity):
        """Get discount percentage for product and quantity"""
        query = """
            SELECT discount_percentage FROM pricing_rules 
            WHERE product_id = %s AND min_quantity <= %s 
            ORDER BY min_quantity DESC LIMIT 1
        """
        result = execute_query(query, (product_id, quantity))
        return result[0]["discount_percentage"] if result else 0
    
    @staticmethod
    def get_tax_rate(region):
        """Get tax rate for region"""
        query = "SELECT tax_rate FROM tax_rates WHERE region = %s"
        result = execute_query(query, (region,))
        return result[0]["tax_rate"] if result else 0
    
    @staticmethod
    def get_all_pricing_rules():
        """Get all pricing rules"""
        query = "SELECT * FROM pricing_rules"
        return execute_query(query)
    
    @staticmethod
    def get_all_tax_rates():
        """Get all tax rates"""
        query = "SELECT * FROM tax_rates"
        return execute_query(query)
    
    @staticmethod
    def create_pricing_rule(product_id, min_quantity, discount_percentage):
        """Create a new pricing rule"""
        query = "INSERT INTO pricing_rules (product_id, min_quantity, discount_percentage) VALUES (%s, %s, %s)"
        return execute_update(query, (product_id, min_quantity, discount_percentage))
    
    @staticmethod
    def add_tax_rate(region, tax_rate):
        """Add tax rate for region"""
        query = "INSERT INTO tax_rates (region, tax_rate) VALUES (%s, %s) ON DUPLICATE KEY UPDATE tax_rate = %s"
        return execute_update(query, (region, tax_rate, tax_rate))
