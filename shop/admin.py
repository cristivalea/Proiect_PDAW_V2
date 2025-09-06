from django.contrib import admin
from .models import Laptop

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('serielaptop', 'brand', 'model', 'pret', 'disponibilitate')
    search_fields = ('brand', 'model', 'procesor')

from .models import Tableta

@admin.register(Tableta)
class TabletaAdmin(admin.ModelAdmin):
    list_display = ('SerieTableta', 'Brand', 'Model', 'pret', 'Disponibilitate')
    search_fields = ('SerieTableta', 'Brand', 'Model')
    list_filter = ('Brand', 'Disponibilitate', 'SistemOperare')


from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.contrib.auth.models import User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('search_users/', self.admin_site.admin_view(self.search_users_view), name='custom_user_search'),
        ]
        return custom_urls + urls

    from django.contrib import admin
    from django.contrib.auth.models import User

    class UserAdmin(admin.ModelAdmin):
        search_fields = ['username', 'email', 'first_name', 'last_name']  # câmpurile pe care vrei să le caute
        list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']

    admin.site.unregister(User)  # dacă e deja înregistrat implicit
    admin.site.register(User, UserAdmin)