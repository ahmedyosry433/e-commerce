from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Product
# Create your views here.

def all_product(request):
    
    all=Product.objects.all()
    
    paginator = Paginator(all ,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'allproduct.html',{'all': page_obj})

def product_detils(request,slug):
    
    details=Product.objects.get(slug=slug)
    
    return render(request , 'product_details.html',{'details':details})
