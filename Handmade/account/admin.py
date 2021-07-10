from django.contrib import admin
from .models import Profile, Address, Celler, CellerAccount
# Register your models here.
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Celler)
admin.site.register(CellerAccount)
