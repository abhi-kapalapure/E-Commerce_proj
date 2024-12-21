from django.urls import path,include
from .views import addcart

urlpatterns = [
    path("",addcart,name="addcart")
]