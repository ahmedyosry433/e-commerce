from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Product
# Create your views here.

def all_product(request):
    
    all=Product.objects.all()
    
    paginator = Paginator(all ,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'all_product.html',{'all': page_obj})

def product_detils(request,id):
    
    details=Product.objects.get(id=id)
    
    return render(request , 'product_details.html',{'details':details})

def t_shirts(request):
    
    all =  Product.objects.filter(category__id = 2)
    return render(request , 't-shirts.html',{'all':all})

def shoses(request):
    
    all =  Product.objects.filter(category__id = 1)
    return render(request , 'shoses.html',{'all':all})