from django.shortcuts import render
from entities import 
# Create your views here.

def order_detail(request, id):
    return render(request, 'order_detail.html')
