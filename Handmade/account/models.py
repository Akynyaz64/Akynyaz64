from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    Gender = (
        ('Erkek', 'Erkek'),
        ('Zenan', 'Zenan'),
    )
    Velayat = (
        ('Aşgabat', 'Aşgabat'),
        ('Balkan', 'Balkan'),
        ('Ahal', 'Ahal'),
        ('Mary', 'Mary'),
        ('Lebap', 'Lebap'),
        ('Daşoguz', 'Daşoguz'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Avatar', upload_to='account/profiles/', blank=True)
    phone = models.CharField('Phone Number', max_length=64)
    gender = models.CharField(choices=Gender, max_length=5, default='Erkek')
    bio = models.TextField('Biography', blank=True)
    age = models.PositiveSmallIntegerField('Age', null=True)
    velayat = models.CharField(choices=Velayat, max_length=10, default='Aşgabat')
    country = models.CharField('Country', max_length=64)
    is_celler = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ('-created', )

class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    extra_phone = models.CharField('Extra Phone', max_length=24)
    address = models.TextField('Address')
    is_active = models.BooleanField(default='True')
    created = models.DateTimeField(auto_now_add=True)

class Celler(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='celler')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.profile.user.username

class CellerAccount(models.Model):
    celler = models.ForeignKey(Celler, on_delete=models.CASCADE, related_name='celler_account')
    subcategory = models.ForeignKey("home.SubCategory", on_delete=models.CASCADE, related_name='celler_accounts')
    title = models.CharField('Title', max_length=64)
    phone = models.CharField('Phone', max_length=24)
    image = models.ImageField('Image', upload_to='celler_account/', blank=True)
    description = models.TextField('Description', blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
