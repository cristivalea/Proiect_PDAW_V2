from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include


from shop.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # Ruta principală către aplicația "shop"
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]