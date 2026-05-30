from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def order(request, **kwargs):
    table_no = kwargs.get("table_no", "parcel")
    item = kwargs.get("item")
    return HttpResponse(f"Order for table {table_no} is {item}")

