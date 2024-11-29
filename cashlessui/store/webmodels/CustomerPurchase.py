from django.db import models
from .StoreProduct import StoreProduct
from cashlessui.models import Customer

class CustomerPurchase(models.Model):
    """Represents a customer purchasing a product.
    Attributes:
    - **product** (*StoreProduct*): The product being purchased. Links to *StoreProduct*.
    - **quantity** (*int*): The quantity of the product purchased.
    - **purchase_price** (*Decimal*): The price the product was purchased for.
    - **customer** (*Customer*): The customer who made the purchase. Links to *Customer*.
    - **customer_balance** (*Decimal*): The customer's balance after the deposit.
    - purchase_date (*DateTime*): The date the deposit was made.
    
    """
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(StoreProduct, on_delete=models.CASCADE)
    # The quantity of the product purchased
    quantity = models.PositiveIntegerField()
    # The price the product was purchased for
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    # The customer who made the purchase
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,  db_constraint=False )
    # The customer's balance after the deposit
    customer_balance = models.DecimalField(max_digits=10, decimal_places=2)
    # The date the deposit was made
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} purchased {self.quantity} x {self.product.name}"


