from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User,Role,Permission
# Register your models here.
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(User)