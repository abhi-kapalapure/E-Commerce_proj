from django.urls import path,include
from .views import order_confirm

urlpatterns = [
    path("", order_confirm, name="order_confirm")
]