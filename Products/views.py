from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Cart,Product

# Create your views here.
def home(request):
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Acoount created successfully! please log in.")
            return redirect('login')
    else:
        form = SignupForm()

    return render(request,"Signup.html",{'form':form})

def login_view(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    else:
        messages.error(request,"Invalid username or password")

    return render(request,'Login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def main_page(request):
    products=Product.objects.all()
    return render(request,"main_page.html",{"products":products})

def product_listing(request):
    return render(request,"product_listing.html")

@login_required(login_url='login')
def cart(request):
    cart_items = cart.objects.filter(user=request.user)
    total = sum(item.subtotal for item in cart_items)
    return render(request,"cart.html",{'cart.items':cart_items,'total':total})