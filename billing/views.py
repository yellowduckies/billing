from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Product
# Create your views here.

def index(request):
    return HttpResponse("mohit")

def fetch_details(request):
    product = list(Product.objects.all().values())
    return JsonResponse(product,safe=False)