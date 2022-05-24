from inspect import trace
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
USER_ROLE = (
        ("emp", 'employee'),
        ("cus", 'customer'),
    )
class MyUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_role = models.CharField(max_length=3,choices=USER_ROLE,default="cus")
    def __str__(self):
        return self.user.username

class Product(models.Model):
    product_name = models.CharField(max_length=254, default= None)
    product_code = models.CharField(max_length=16,null=True,blank=True,editable=False)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name+" "+self.product_code
    
    def save(self,*args, **kwargs):
        self.product_code = (self.product_name[0:3]).upper()+str(self.pk).zfill(13)
        super(Product, self).save(*args, **kwargs)
    

class Invoice(models.Model):
    customer = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    invoice_number = models.CharField(max_length=254,default=None,null=True,blank=True,editable=False)
    product_code = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    total_amount = models.FloatField(default=0,null=True,blank=True,editable=False)
    invoice_date_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer.user.username +" "+self.invoice_number
    # def save(self,*args, **kwargs):
    #     self.invoice_number = (self.created_at).strftime('%Y%m%d%H%M').upper()+str(self.pk)
    #     self.total_amount = self.quantity*self.product_code.price
    #     super(Invoice, self).save(*args, **kwargs)
    



