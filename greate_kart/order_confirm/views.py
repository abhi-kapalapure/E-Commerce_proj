from django.shortcuts import render

def order_confirm(request):
    return render(request,'order_confirm.html')
