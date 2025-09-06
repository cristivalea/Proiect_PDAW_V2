from django.urls import path
from django.contrib.auth import views as auth_views

from shop import views

urlpatterns = [
    path('', views.index, name='index'),  # Pagina principală cu lista de laptopuri
    path('produs/<str:serielaptop>/', views.product_detail, name='product_detail'),  # Detalii despre un laptop
    path('cart/', views.cart, name='cart'),  # Coșul de cumpărături (temporar simplu)
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    #path('profil/', views.profil_utilizator, name='profil_utilizator'),
]