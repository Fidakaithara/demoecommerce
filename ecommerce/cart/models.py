from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model): #cart table definition
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)


    def subtotal(self):
        return self.quantity*self.product.price



class Payment(models.Model):
    name=models.CharField(max_length=30)
    amount=models.IntegerField()
    order_id=models.CharField(max_length=30,blank=True)
    razorpay_payment_id=models.CharField(max_length=30)
    paid=models.BooleanField(default=False)



class Order_details(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_items=models.IntegerField()
    address=models.TextField()
    phone=models.BigIntegerField()
    pin=models.IntegerField()

    order_id=models.CharField(max_length=30,blank=True)
    ordered_date=models.DateTimeField(auto_now_add=True)

    payment_status=models.CharField(max_length=30,default="pending")
    delivery_status=models.CharField(max_length=30,default="pending")




