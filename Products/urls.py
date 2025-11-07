from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Signup/',views.signup,name='signup'),
    path('Login/',views.login_view,name='login'),
    path('main_page/',views.main_page,name='main_page'),
    path('product_listing/',views.product_listing,name='product_listing'),
    path('cart/',views.cart,name='cart'),
    path('logout/',views.logout_view,name="logout"),
]