from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    address=models.TextField()
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100,default="user")
    
    def __str__(self):
        return self.fname+" - "+self.usertype
    
class Product(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    product_price=models.PositiveIntegerField()
    product_image=models.ImageField(upload_to="product_images/")
    product_desc=models.TextField()
    
    def __str__(self):
        return self.seller.fname+"-"+self.product_name
    
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.fname+" - "+self.product.product_name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    product_price=models.PositiveIntegerField()
    product_qty=models.PositiveIntegerField(default=1)
    total_price=models.PositiveIntegerField()
    shipping=models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.user.fname+" - "+self.product.product_name