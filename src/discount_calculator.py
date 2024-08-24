from datetime import datetime, timedelta

class DiscountCalculator:
    def __init__(self, customer_type: str, join_date: datetime, total_spent: float):
        self.customer_type = customer_type
        self.join_date = join_date
        self.total_spent = total_spent

    def apply_discount(self, base_price: float) -> float:
        discount = 0.0

        if self.customer_type == "VIP":
            discount += 0.2  
        elif self.customer_type == "Regular":
            discount += 0.1  
        elif self.customer_type == "New":
            discount += 0.05  
        
        if self._is_loyal_customer():
            discount += 0.05  

        if self.total_spent > 1000:
            discount += 0.1  

        return base_price * (1 - discount)

    def _is_loyal_customer(self) -> bool:
        """Verifica si el cliente ha sido leal (más de 2 años desde que se unió)."""
        return datetime.now() - self.join_date > timedelta(days=365 * 2)

def calculate_total(products: list[float], discount: bool = False, apply_tax: bool = True) -> float:
    total = sum(products)
    
    if discount:
        total *= 0.9  

    if apply_tax:
        total *= 1.08  

    return total

def is_eligible_for_discount(customer_type: str, total_spent: float) -> bool:
    """Determina si un cliente es elegible para cualquier tipo de descuento."""
    return customer_type in ["VIP", "Regular", "New"] or total_spent > 500
