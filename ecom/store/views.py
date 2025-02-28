from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    products=Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Some error occured, please login again!'))
            return redirect('login')
        

    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('home')

def register_user(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request, username=username, password=password)
            #login
            login(request, user)
            messages.success(request, ('You have logged in successfully'))
            return redirect('home')
    else:
        return render(request, 'register.html',  {'form':form})
    
def product(request, pk):
    product=Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def category(request, cat):
    cat=cat.replace('-', " ")
    try:
        category=Category.objects.get(name=cat)
        products=Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    
    except:
        messages.success(request, ('This category doesnt exists!'))
        return redirect('home')


