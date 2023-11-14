from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth

from django.http import JsonResponse
from django.middleware import csrf



# #class based view to search for products 
# # based on parameters "product name", "product desc" and "product category"
# class ProductList(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     def get_queryset(self):
#         search_product = self.request.query_params.get('search')
#         order = self.request.query_params.get('order')
#         category = self.request.query_params.get('category')
#         queryset1 = Product.objects.filter(name__icontains=search_product)
#         queryset2 = Product.objects.filter(desc__icontains=search_product)
#         #searches for products only if order and category parameter is passed
#         if order is not None:
#             #if "order" parameter has some value ('price' or 'desc') this searches within category
#             #and returns the union of both query sets
#             if category is not None:
#                 queryset3 = Product.objects.filter(category=category)
#                 return queryset1.union(queryset2).union(queryset3).order_by(order)
#             return queryset1.union(queryset2).order_by(order)
        
#         #if 'order' parameter is not passed but 'category is passed
#         elif category is not None:
#             queryset3 = Product.objects.filter(category=category)
#             return queryset1.union(queryset3).order_by("price")
        
#         #to search products with only categories or if 'search parameter is not passed
#         elif search_product is None:
#             return queryset3
        
#         #if 'category' parameter is not passed
#         else:
#             return queryset1.union(queryset2)

# #class based view to get product by "id"
# class ProductView(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     def get(self):
#         pk = self.request.query_params.get('pk')
#         product = Product.objects.get(id=pk)
#         return product
    

# def get_csrf_token(request):
#     csrf_token = csrf.get_token(request)
#     return JsonResponse({'csrfToken': csrf_token})

# class CustomAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         print(request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })

# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def get(self, request, format=None):
#         print(request.user)
#         # user = User.objects.get(request.user)
#         content = {'user': str(request.user),
#                    'auth': str(request.auth),
#                 }
#         return Response(content)

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             user = User.objects.get(username=username)
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({
#                 'user_status': 'logged_in',
#                 'token': token.key,
#                 'id': user.pk,
#                 'username': user.username,
#                 'first_name': user.first_name,
#                 'last_name':user.last_name,
#                 })
#         else:
#             return Response({
#                 'user_status': 'anonymous',
#                 'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
#     def customer_details(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             if Customer.objects.filter(pk=user.pk):
#                 customer = Customer.objects.get(pk=user.pk)
#                 return Response({
#                     'phone': customer.phone,
#                     'address': customer.streetaddr,
#                     'city': customer.city,
#                     'pincode': customer.pincode
#                 })
#             else:
#                 return Response({
#                     'message': 'You have not added more details about yourself'
#                 })

# class RegisterUser(APIView):

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(request, username=username, password=password)
#         if User.objects.filter(username=username).exists():
#             return Response({
#                 'message': 'Please Try with a different Username.'
#             })
#         else:
#             user = User.objects.create_user(
#                 username = username,
#                 password = password,
#             )
#             user.save()
#             login(request, user)
#             token = Token.objects.create(user=user)
#             return Response({
#                 'message': 'User Registered',
#                 'id': user.pk,
#                 'token': token.key,
#                 'username': user.username,
#             })
    
#     def create_customer(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         first_name = request.data.get('first_name')
#         last_name = request.data.get('last_name')
#         email = request.data.get('email')
#         mobile = request.data.get('mobile')
#         streetaddr = request.data.get('address')
#         pincode = request.data.get('pincode')
#         city = request.data.get('city')

#         user = authenticate(request, username=username, password=password)
#         if Customer.objects.filter(phone=mobile).exists():
#                 return Response({
#                     'message': 'This mobile number is already registered'
#                 })
#         elif User.objects.filter(email=email).exists():
#             return Response({
#                 'message': 'Please try with a different email-id.'
#             })
#         else:
#             user = User.objects.get(username=username)
#             user.email = email
#             user.first_name = first_name
#             user.last_name = last_name
#             user.save()
#             customer = Customer.objects.create(
#                 pk = user.pk,
#                 streetaddr = streetaddr,
#                 phone = mobile,
#                 city = city,
#                 pincode = pincode,
#             )
#             login(request, user)
#             return Response({
#                 'message': 'User Registered',
#                 'id': user.pk,
#                 'username': user.username,
#                 'first_name': customer.first_name,
#                 'last_name': customer.last_name,
#                 'email': user.email,
#                 'mobile': customer.phone,
#                 'streetaddr': customer.streetaddr,
#                 'city': customer.city,
#                 'pincode': customer.pincode
#             })


# Create your views here.

def index(request):
    context = {'logo': "Store"}
    return render(request, 'index.html', context)

def home(request):
    #to display the home page
    return render(request,'home.html')


def profile(request):
    #to go to profile page of the user
    context = {'logo': "user"}
    return render(request, 'profile.html', {'logo': "STORE"})

#user login form
def user_login(request):
    #gets form input only if the form action method is POST
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        #this function works only if user is not logged in 
        if user is not None:
            login(request,user)
            print("logged in")
            messages.success(request,'Logged In')
            return redirect('home')
        else:
            messages.warning(request,'Invalid Credentials. Try again.')
        return redirect('home')
    

#user registration form
def signup(request):
    #gets form input only if the form action method is POST
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        #checks if email is already registered or not,
        #if already registred email found, it sends a message and redirects to login
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email already registered. Login or try another email.')
            return redirect('user_login')
        
        #checks if username is already registered or not,
        #if already registred username found, it sends a message and redirects to login
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username has been used already, Try Logging in.')
            return redirect('user_login')
        #if all credentials are valid a user object is created
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                
            )
            user.save()
            # user = auth.authenticate(request,username=username,password=password)    #to save the new user object
            login(request,user)  #to log in the new user
            messages.success(request,"Congrats🎉!! Your are a new member to us.😉")
            return redirect('home')

def products(request):
    # #fetch out the products from the database with the filter
    # search_product = request.GET['product']
    # # products_list = Product.objects.filter(name__contains=search_product)
    # products_list = list(products_list)
    # if len(products_list)!=0:
    #     #counts the number of products found in the database
    #     num_of_products = len(products_list)
    #     return render(request,'products.html',{'products':products_list,'num_of_products':num_of_products,'search':search_product})

    # else:
    #     #returns nothing if no products found with the relevant name
    #     num_of_products = 'No'
    #     return render(request, 'products.html',{'num_of_products':num_of_products})
    return render(request, 'product.html', {'logo':'STORE'})

def products_by_category(request):
    #fetch products from the database wy filtering through categories
    pass

def create_order(request):
    pass


def user_logout(request):
    #to logout the user
    logout(request)
    messages.info(request,"Logged Out.")
    return redirect('home')

def delete_account(request):
    #to delete the user account
    try:
        username = request.user.username
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        user.delete()
        messages.success(request,"User deleted. Redirecting you to home.")
        return redirect(request,'home')
    except User.DoesNotExist:
        messages.error(request,"User does not exists.")
        return redirect(request,'home')
