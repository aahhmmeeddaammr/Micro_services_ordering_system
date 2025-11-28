from ..models import PricingRule


def get_all_pricing_rules():
    """Get all pricing rules"""
    try:
        rules = PricingRule.get_all_pricing_rules()
        return {
            "success": True,
            "rules": rules if rules else []
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

