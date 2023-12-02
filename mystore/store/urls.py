from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home root default'),
    path('home/', views.index, name='home root default'),
    path('product/',views.products, name='products page'),
    path('profile/',views.profile, name='user profile'),
    path('logout/',views.user_logout, name="user logout"),
    path('cart/',views.cart,name="cart page for user"),
    path('checkout/<int:id>/',views.checkout, name="checkout page"),
    path('login/',views.user_login,name="user login"),
    path('create-order-item/',views.create_order_item,name="add item to order item"),
    path('confirm-order/', views.confirm_order, name="create order for user"),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
