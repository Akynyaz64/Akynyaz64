from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField('Title', max_length=64)
    icon = models.CharField('Icon', max_length=64)
    image = models.ImageField('Image', upload_to='category/', blank=True)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    title = models.CharField('Title', max_length=64)
    icon = models.CharField('Icon', max_length=64)
    image = models.ImageField('Image', upload_to='subcategory/', blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    celler_account = models.ForeignKey("account.CellerAccount", on_delete=models.CASCADE, related_name='products')
    title = models.CharField('Title', max_length=64)
    image = models.ImageField('Image', upload_to='product/', blank=False)
    price = models.PositiveSmallIntegerField('Price', default=0)
    description = models.TextField('Description')
    views = models.PositiveSmallIntegerField('Views', default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.title
