from datetime import datetime
from time import strftime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from .models import Invoice, Product
# Create your views here.

def index(request):
    return HttpResponse("mohit")

def fetch_details(request):
    product = list(Product.objects.all().values())
    return JsonResponse(product,safe=False)

@csrf_exempt
def fetch_by_date(request):
    date = request.POST.get("date")
    if request.method != 'POST':
        # pass date in format 2022-06-01
        return HttpResponse("This API accepts only POST request with date")
    else:
        if date == None:
            return HttpResponse("No date given")
        else:
            invoice_on_date = Invoice.objects.filter(invoice_date_time__contains=str(date))
            invoice_count = len(invoice_on_date)
            total_items_sold = 0
            total_amount = 0

            for i in invoice_on_date:
                total_items_sold+=i.quantity
                total_amount+=i.total_amount
            params = {
                'invoice_count':invoice_count,
                'total_items_sold':total_items_sold,
                'total_amount':total_amount
            }
            return JsonResponse(params)