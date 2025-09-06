from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label="Prenume")
    last_name = forms.CharField(max_length=30, required=False, label="Nume")
    email = forms.EmailField(required=True, label="Email")
    is_admin = forms.BooleanField(required=False, label="Administrator")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']



from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    #cantitate = forms.IntegerField(min_value=1, label="Cantitate")  # câmp suplimentar, nu în model

    class Meta:
        model = Laptop
        exclude = ['nota_produs']

from .models import Tableta
class TabletaForm(forms.ModelForm):
    class Meta:
        model = Tableta
        exclude = ['NotaProdus']

from .models import Telefon
class TelefonForm(forms.ModelForm):
    class Meta:
        model = Telefon
        exclude = ['NotaProdus']


from django import forms

class OrderForm(forms.Form):
    payment_method = forms.ChoiceField(choices=[('card', 'Card'), ('ramburs', 'Ramburs')])
    shipping_address = forms.CharField(widget=forms.Textarea)

from django import forms
from .models import Order

class ComandaForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'total', 'status']  # fără 'order_date'


