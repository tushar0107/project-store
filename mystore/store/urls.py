from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home root default'),
    path('home/', views.index, name='home root default'),
    path('product/',views.products, name='products page'),
    path('product/<str:slug>',views.product, name='products page'),
    path('profile/',views.profile, name='user profile'),
    path('logout/',views.user_logout, name="user logout"),
    path('update-cart/',views.update_cart,name="cart page for user"),
    path('cart/',views.cart,name="cart page for user"),
    path('checkout/',views.checkout, name="checkout page"),
    path('checkout/<int:id>/',views.checkout, name="checkout page"),
    path('login/',views.user_login,name="user login"),
    path('register/',views.signup, name='user registration'),
    path('create-order-item/',views.create_order_item,name="add item to order item"),
    path('confirm-order/', views.confirm_order, name="create order for user"),
    path('get-csrf-token/', views.get_csrf_token, name='token'),
    path('api/product/<int:pk>/', views.ProductView.as_view(), name='to get product by id'),
    path('api/products/', views.ProductListView.as_view({'get':'list'}),name='to get product list'),
    path('api/login/<int:id>',views.LoginView.as_view(), name='to login for a user'),
    path('api/login/',views.LoginView.as_view(), name='to login for a user'),
    path('api/register/',views.RegisterUser.as_view(), name='to register new user'),
    path('api/create-customer/',views.CustomerCreate.as_view(), name='to create customer for a user'),
    

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
