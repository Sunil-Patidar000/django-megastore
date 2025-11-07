from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    short_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/',blank=True , null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE,related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    @property
    def subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"
