from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
    ('Vinnytsia Oblast', 'Vinnytsia Oblast'),
    ('Volyn Oblast', 'Volyn Oblast'),
    ('Dnipropetrovsk Oblast', 'Dnipropetrovsk Oblast'),
    ('Donetsk Oblast', 'Donetsk Oblast'),
    ('Zhytomyr Oblast', 'Zhytomyr Oblast'),
    ('Zakarpattia Oblast', 'Zakarpattia Oblast'),
    ('Zaporizhzhia Oblast', 'Zaporizhzhia Oblast'),
    ('Ivano-Frankivsk Oblast', 'Ivano-Frankivsk Oblast'),
    ('Kyiv Oblast', 'Kyiv Oblast'),
    ('Kirovohrad Oblast', 'Kirovohrad Oblast'),
    ('Luhansk Oblast', 'Luhansk Oblast'),
    ('Lviv Oblast', 'Lviv Oblast'),
    ('Mykolaiv Oblast', 'Mykolaiv Oblast'),
    ('Odessa Oblast', 'Odessa Oblast'),
    ('Poltava Oblast', 'Poltava Oblast'),
    ('Rivne Oblast', 'Rivne Oblast'),
    ('Sumy Oblast', 'Sumy Oblast'),
    ('Ternopil Oblast', 'Ternopil Oblast'),
    ('Kharkiv Oblast', 'Kharkiv Oblast'),
    ('Kherson Oblast', 'Kherson Oblast'),
    ('Khmelnytskyi Oblast', 'Khmelnytskyi Oblast'),
    ('Cherkasy Oblast', 'Cherkasy Oblast'),
    ('Chernivtsi Oblast', 'Chernivtsi Oblast'),
    ('Chernihiv Oblast', 'Chernihiv Oblast'),
    ('Autonomous Republic of Crimea', 'Autonomous Republic of Crimea'),
    ('Kyiv', 'Kyiv'),
    ('Sevastopol', 'Sevastopol')
)

CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('PN', 'Panner'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('MC', 'Milkshake'),
    ('IC', 'Ice-Creams'),


)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
       return self.quantity * self.product.discounted_price