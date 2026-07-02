from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Cart,Product,Seller
from django.contrib.auth.models import User

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
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request,"cart.html",{'cart_items':cart_items,'total':total})

@login_required(login_url='/login')
def add_to_cart(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    cart_item,created = Cart.objects.get_or_create(user=request.user,product=product)

    if not created:
        cart_item.quantity +=1
        cart_item.save()

    return redirect('cart_view')

@login_required(login_url='login')
def place_order(request):
    Cart.objects.filter(user=request.user).delete()
    return render(request,"order_success.html")


def seller_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        store_name = request.POST.get('store_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect('seller_signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        Seller.objects.create(user=user, store_name=store_name, phone=phone, address=address)
        messages.success(request, 'Account created! Please login.')
        return redirect('seller_login')

    return render(request, 'seller_signup.html')

def seller_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('seller_dashboard')
        else:
            messages.error(request, 'Invalid credentials!')
    return render(request, 'seller_login.html')


@login_required(login_url='seller_login')
def seller_dashboard(request):
    # Check if session user is valid
    if not request.user.is_authenticated or not isinstance(request.user, User):
        messages.error(request, "Invalid session. Please log in again.")
        logout(request)
        return redirect('seller_login')

    # Try to fetch seller profile
    seller = Seller.objects.filter(user=request.user).first()
    if not seller:
        messages.error(request, "Seller profile not found. Please register first.")
        return redirect('seller_signup')

    # Fetch products related to this seller
    products = Product.objects.filter(seller=seller)

    # Render dashboard
    return render(request, 'seller_dashboard.html', {
        'seller': seller,
        'products': products
    })


@login_required(login_url='seller_login')
def seller_logout(request):
    logout(request)
    return redirect('seller_login')



