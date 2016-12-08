from django.shortcuts import render

# Create your views here.

def order_detail(request, id):
    return render(request, 'order_detail.html')
