from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered', 'Delivered'),
)
MODES = (
    ('COD', 'COD'),
    ('Debit/Credit Card','Debit/Credit Card'),
    ('UPI','UPI'),
)
PAY_STATUS = (
    
    ('Paid','Paid'),
    ('Pending','Pending')
)
CITIES = (('Nagpur','Nagpur'),
              ('Pune','Pune'),
              ('Nashik','Nashik'),
              ('Aurangabad','Aurangabad'),
              ('Wardha','Wardha'))
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate the slug from the name field if it's not set
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=300,default='')
    desc = models.TextField()
    brand = models.CharField(max_length=30,default='none')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', default='')
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return str(f'[{self.pk}] {self.name}')
    
    def getBrand(self):
        return self.brand

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.BigIntegerField()
    plot_no = models.TextField(default='')
    streetaddr = models.TextField()
    city = models.CharField(max_length=20, choices=CITIES)
    pincode = models.PositiveIntegerField()
    
    def _str__(self):
        return str(f'{self.user}')
    
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1',)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default='')
    quantity = models.PositiveIntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    details = models.TextField(default='',blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(f'Order by ,{self.user.username}')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    order = models.ManyToManyField(OrderItem)
    delivery_address = models.CharField(max_length=300, default='none')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=20,choices=MODES, default='1')
    payment_status = models.CharField(max_length=20,choices=PAY_STATUS, default='Pending')
    order_status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='Pending')
    def __str__(self):
        return str(f'{self.user.username} : payment {self.payment_status}')

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=MODES)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=20, choices=PAY_STATUS)

    def __str__(self):
        return f"Payment for Order #{self.pk} is {self.payment_status} via {self.payment_method}"
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return str(f'{self.rating} rating by {self.user.username} for {self.product.name}')
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(f"{self.user.first_name}'s Cart: {self.product.name}")