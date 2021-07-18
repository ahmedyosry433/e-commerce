from django.urls import path
from . import views
app_name = 'Product'

urlpatterns = [
    path('allproduct/', views.all_product, name='allproduct' ),
    path('t-shirts/', views.t_shirts, name='t_shirts' ),
    path('shoses/', views.shoses, name='shoses' ),
    path('detials/<int:id>', views.product_detils, name='details' ),
]
