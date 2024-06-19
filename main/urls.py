from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index_view, name="index_url"),
    path('about/', about_view, name="about_url"),
    path('shop/', shop_view, name="shop_url"),
    path('product/',product_view, name="product_url"),
    path('cart/', cart_view, name="cart_url"),
    path('checkout/', checkout_view, name="checkout_url"),
    path('wishlist/', wishlist_view, name="wishlist_url"),
    path('blog/', blog_view, name="blog_url"),
    path('blog-details/', blogdetails_view, name="blog-details_url"),
    path('contact/', contact_view, name="contact_url"),
    ]