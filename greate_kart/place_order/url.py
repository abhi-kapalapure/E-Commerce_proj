from django.urls import path,include
from .views import place_order

urlpatterns = [

    path("", place_order, name="place_order")
]