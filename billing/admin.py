from django.contrib import admin
from .models import Invoice, MyUser, Product

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Product)
admin.site.register(Invoice)