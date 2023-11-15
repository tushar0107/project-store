from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home root default'),
    path('index', views.index, name='home root default'),
    path('profile',views.profile, name='home page'),
    path('product',views.products, name='products page'),
    path('logout', views.logout, name="user logout"),
    path('profile',views.profile, name='user profile'),
    path('logout',views.logout, name="user logout"),
    path('cart',views.cart,name="cart page for user"),
    path('checkout',views.checkout, name="checkout page"),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
