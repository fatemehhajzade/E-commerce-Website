from django.contrib import admin
from . import models
from django.contrib.auth.models import User

admin.site.register(models.Product)
admin.site.register(models.Category)    
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.Profile)

# admin can see user profile when click on a user(personalize admin panel)
class ProfileInline(admin.StackedInline):
    model = models.Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password']
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)