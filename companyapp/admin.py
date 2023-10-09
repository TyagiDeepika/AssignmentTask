from django.contrib import admin
from .models import User,Company


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(User, UserAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Company, CompanyAdmin)