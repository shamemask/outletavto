from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myapp.UserModel import FizUser, UrUser

# Register your models2 here.
admin.site.register(FizUser)
admin.site.register(UrUser)
