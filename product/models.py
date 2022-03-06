from django.db import models
from helper.some_model import CrUpBase
import uuid
from authen.models import Account
# Create your models here.
"""
    1. Banner/Carousel 
    2. Advertisement/Announcement
    3. Product Category
    4. Product Sub Category
    5. Product Size
    6. Product
    7. AdditionalProductDescription
    8. ProductReview

    1. Wishlist
    2. Cart
    3. Order
    4. Delievery

"""

class Banner(models.Model):
    title = models.CharField(max_length=200)
    landscape_image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Announcement(CrUpBase):
    start_date = models.DateField()
    end_date = models.DateField()
    landscape_image = models.ImageField()
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Category(CrUpBase):
    title = models.CharField(max_length=200)
    description = models.TextField()
    portrait_image = models.ImageField()
    banner_image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
class SubCategory(CrUpBase):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField()
    portrait_image = models.ImageField()
    banner_image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

class ProductSize(CrUpBase):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Product(CrUpBase):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField()
    size = models.ManyToManyField(ProductSize, blank=True)
    is_available = models.BooleanField(default=True)
    price = models.FloatField()
    cut_price = models.FloatField()
    customizable = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.title}: {self.price}"

# class AdditionalProductDescription(models.Model):
#     product = models.OneToOneField(Product, on_delete=models.CASCADE)
#     cloth_type = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return f"{self.product.title}"

RATING = (
   ('1', '1'),
   ('2', '2'),
   ('3', '3'),
   ('4', '4'),
   ('5', '5')
)
class ProductReview(CrUpBase):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    rating = models.CharField(max_length=2, choices=RATING)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.product.title}: {self.title}"

class Wishlist(CrUpBase):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)

# class Order(CrUpBase)