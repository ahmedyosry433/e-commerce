from django.shortcuts import redirect, render
from django.contrib.auth import login , authenticate
from django.shortcuts import get_object_or_404
from .forms import *
from .models import Customer
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username , password=password)
            user = form.save()
            login(request , user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/product')
        
    else : 
        form = SignupForm()
        
    return render (request,'registration/signup.html',{'form':form} )

def profile (request ,slug):
    profile =get_object_or_404 (Customer,slug=slug)
    
    return render(request , 'registration/profile.html' , {'profile':profile})