from django.contrib import admin
from accounts.models import UserProfile #always have to import model
# Register your models here.


#This is display our model in the admin site
admin.site.register(UserProfile)
