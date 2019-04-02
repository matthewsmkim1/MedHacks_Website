from django.contrib import admin
from accounts.models import UserProfile #always have to import model

#Add class to add more columsn in admin view
class UserProfileAdmin(admin.ModelAdmin):
    #this tuple displays the ordering in the admin page as well
    list_display = ('user', 'user_info', 'city', 'website', 'phone')

    def user_info(self, obj):
        return obj.description

    #if we want to change the name of what appears in the django admin page
    user_info.short_description = 'info'
#This is display our model in the admin site
admin.site.register(UserProfile, UserProfileAdmin)
