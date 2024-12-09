from django.db import models
from .StoreProduct import StoreProduct
from store.webmodels.Customer import Customer

from .ProductInventory import ProductInventory
from decimal import Decimal

import logging

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
    # The total price the product was purchased for
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    # The total expenses incurred by the purchase
    expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # The total revenue generated by the purchase
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # The customer who made the purchase
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,  db_constraint=False )
    # The customer's balance after the deposit
    customer_balance = models.DecimalField(max_digits=10, decimal_places=2)
    # The date the deposit was made
    purchase_date = models.DateTimeField(auto_now_add=True)

    def get_all_purchases(product: StoreProduct):
        return CustomerPurchase.objects.filter(product=product)
    
    def get_all_purchases_aggregated(product: StoreProduct):
        return CustomerPurchase.objects.filter(product=product).aggregate(models.Sum('quantity'))['quantity__sum']
    
    # function that is called, every time a new CustomerPurchase object is created
    def save(self, *args, **kwargs):
        logging.getLogger('store').info(f"[PURCHASE] New purchase: {self}")
        super().save(*args, **kwargs)

  
    def calculate_revenue(self):
        """Calculates revenue based on FIFO inventory usage."""
        quantity_to_allocate = self.quantity
        total_cost = Decimal(0)

        inventory_items = ProductInventory.objects.filter(
            restock__product=self.product, remaining_quantity__gt=0
        ).order_by('restock__restock_date')
        print(f"Inventory items: {inventory_items}")

        for inventory in inventory_items:
            if quantity_to_allocate <= 0:
                break
            if inventory.remaining_quantity >= quantity_to_allocate:
                total_cost += quantity_to_allocate * inventory.restock.purchase_price
                print(f"total cost {total_cost}: {quantity_to_allocate} - {inventory.restock.purchase_price}")
                inventory.remaining_quantity -= quantity_to_allocate
                inventory.save()
                quantity_to_allocate = 0
            else:
                total_cost += inventory.remaining_quantity * inventory.restock.purchase_price
                print(f"total cost {total_cost}: {quantity_to_allocate} - {inventory.restock.purchase_price}")
                quantity_to_allocate -= inventory.remaining_quantity
                inventory.remaining_quantity = 0
                inventory.save()

        self.expenses = total_cost
        self.revenue = (self.purchase_price * self.quantity) - total_cost
        self.save()

    def save(self, *args, **kwargs):
        """Override save to calculate revenue."""
        super().save(*args, **kwargs)
        #self.calculate_revenue()

    def __str__(self):
        return f"{self.customer.user.first_name} {self.customer.user.last_name}: {self.quantity} x {self.product.name} = {self.purchase_price}"

    def __str__(self):
        return f"Purchase of {self.quantity} x {self.product.name} by {self.customer.user.username}"
