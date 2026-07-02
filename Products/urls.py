from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Signup/',views.signup,name='signup'),
    path('Login/',views.login_view,name='login'),
    path('main_page/',views.main_page,name='main_page'),
    path('product_listing/',views.product_listing,name='product_listing'),
    path('cart/',views.cart_view,name='cart_view'),
    path('logout/',views.logout_view,name="logout"),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('place_order/',views.place_order,name='place_order'),
    path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('seller/signup/', views.seller_signup, name='seller_signup'),
    path('seller/login/', views.seller_login, name='seller_login'),
    path('seller_logout/', views.seller_logout, name='seller_logout'),
]