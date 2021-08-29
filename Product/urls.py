from django.urls import path
from . import views
app_name = 'Product'

urlpatterns = [
    path('', views.all_product, name='allproduct' ),
    path('<slug:slug>', views.product_detils, name='details' ),
]
