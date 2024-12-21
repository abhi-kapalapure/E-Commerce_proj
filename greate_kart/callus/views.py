from django.shortcuts import render

# Create your views here.
def call_us(request):
    return render(request,'callus.html')

