import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/Products/')

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)
    @staticmethod
    def get_all_object():
        return Product.objects.all()
    @staticmethod
    def get_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_object()
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone=models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False

    @staticmethod
    def get_customer_by_email( email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False


class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity =models.IntegerField(null=True)
    price = models.IntegerField()
    address = models.CharField(max_length=50,blank=True,default='',null=True)
    phone = models.CharField(max_length=50,blank=True,default='',null= True)
    date = models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customers(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')