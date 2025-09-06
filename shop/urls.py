from django.contrib.auth.views import LogoutView
from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views

from shop.views import CustomLoginView

urlpatterns = [
    path('', views.index, name='index'),  # Pagina principală cu lista de laptopuri
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('register/', views.register, name='register'),

    path('admin-dashboard/adaugare_laptop/', views.adaugare_laptop, name='adaugare_laptop'),
    path('admin-dashboard/cautare_laptop/', views.cautare_laptop, name='cautare_laptop'),
    path('delete-laptop/', views.delete_laptop, name='delete_laptop'),
    path('edit-laptop/<str:serielaptop>/', views.edit_laptop, name='edit_laptop'),

    path('admin-dashboard/adauga_tableta/', views.adauga_tableta, name='adauga_tableta'),
    path('admin-dashboard/cautare_tableta/', views.cautare_tableta, name='cautare_tableta'),
    path('edit_tableta/<str:serietableta>/', views.edit_tableta, name='edit_tableta'),
    path('delete_tableta/', views.delete_tableta, name='delete_tableta'),

    path('admin-dashboard/adaugare_telefoan/', views.adaugare_telefon, name='adaugare_telefon'),
    path('admin-dashboard/cautare_telefon/', views.cautare_telefon, name='cautare_telefon'),
    path('edit_telefon/<str:serie>/', views.editare_telefon, name='edit_telefon'),
    path('delete_telefon/', views.delete_telefon, name='delete_telefon'),

    path('admin-dashboard/cautare_utilizatori', views.cauta_utilizatori, name='cautare_utilizatori'),
    path('admin-dashboard/sterge_utilizator/<int:user_id>/', views.sterge_utilizator, name='sterge_utilizator'),
    path('admin-dashboard/editare_utilizator/<int:user_id>/', views.editare_utilizator, name='editare_utilizator'),

    path('', views.index, name='index'),
    path('login/', views.custom_login, name='login'),
    path('laptopuri/', views.lista_laptopuri, name='laptopuri'),
    path('laptopuri/<str:serielaptop>/', views.detalii_laptop, name='detalii_laptop'),
    path('tablete/', views.lista_tablete, name='tablete'),
    path('tablete/<str:serietableta>/', views.detalii_tableta, name='detalii_tableta'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profil/', views.user_profile, name='user_profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path("telefoane/", views.lista_telefoane, name="lista_telefoane"),
    path("telefoane/<str:serie>/", views.detalii_telefon, name="detalii_telefon"),
    path('cos/', views.view_cart, name='view_cart'),
    path('adauga-in-cos/<str:product_type>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('sterge-din-cos/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    # path('admin-dashboard/cauta-comenzi/', views.cauta_comenzi_dupa_user, name='cautare_comenzi'),
    # path('comanda/update/<int:pk>/', views.update_comanda, name='update_comanda'),
    # path('comanda/delete/<int:pk>/', views.delete_comanda, name='delete_comanda'),

    path('admin-dashboard/cauta-comenzi/', views.cauta_comenzi_dupa_user, name='cauta_comenzi_dupa_user'),

    # URL-ul pentru editare comandă
    path('admin-dashboard/comanda/edit/<int:pk>/', views.update_comanda, name='update_comanda'),

    # URL-ul pentru ștergere comandă
    path('admin-dashboard/comanda/delete/<int:pk>/', views.delete_comanda, name='delete_comanda'),
]
