from django.urls import path,include
from .views import call_us

urlpatterns = [
    path("",call_us,name='call_us')
]