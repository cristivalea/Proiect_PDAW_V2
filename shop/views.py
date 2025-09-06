# from django.shortcuts import render, get_object_or_404
# from .models import Laptop
# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.contrib.auth.models import User
#
#
# # def index(request):
# #     laptops = Laptop.objects.all()
# #     context = {
# #         'laptops': laptops
# #     }
# #     return render(request, 'shop/index.html', context)
#
# def index(request):
#     return render(request, 'shop/index.html')
# def product_detail(request, serielaptop):
#     laptop = get_object_or_404(Laptop, serielaptop=serielaptop)
#     context = {
#         'laptop': laptop
#     }
#     return render(request, 'shop/product_detail.html', context)
#
# def cart(request):
#     # Pentru început, o pagină simplă, se poate extinde ca funcționalitate de coș.
#     return render(request, 'shop/cart.html')
#
#
#
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import CustomUserCreationForm, TelefonForm
#
#
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)  # Nu salvăm încă în DB
#             # Adăugăm câmpurile suplimentare
#             user.first_name = form.cleaned_data.get('first_name')
#             user.last_name = form.cleaned_data.get('last_name')
#             user.email = form.cleaned_data.get('email')
#             if form.cleaned_data.get('is_admin'):
#                 user.is_staff = True
#             user.is_active = True  # În caz că vrei să gestionezi activarea manual
#             user.save()
#
#             messages.success(request, 'Contul a fost creat cu succes! Te poți loga acum.')
#             return redirect('login')
#         else:
#             print("Erori formular:", form.errors)
#             messages.error(request, 'Ceva nu a mers bine. Te rugăm să încerci din nou.')
#     else:
#         form = CustomUserCreationForm()
#
#     return render(request, 'shop/register.html', {'form': form})
#
#
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
#
#
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             if user.is_superuser or user.is_staff:
#                 # Dacă este admin sau staff, redirecționează către pagina de admin
#                 return redirect('admin_dashboard')  # O pagină specială pentru admini
#             else:
#                 # Dacă e utilizator normal
#                 return redirect('/')
#         else:
#             # Dacă username sau parola sunt greșite
#             return render(request, 'shop/login.html', {'error': 'Utilizator sau parolă greșită'})
#
#     return render(request, 'shop/login.html')
#
# from django.contrib.auth.decorators import login_required, user_passes_test
#
# @login_required
# @user_passes_test(lambda u: u.is_staff or u.is_superuser)
# def admin_dashboard(request):
#     return render(request, 'shop/admin_dashboard.html')
#
# from django.shortcuts import render, redirect
# from .forms import LaptopForm
#
#
# def adaugare_laptop(request):
#     if request.method == 'POST':
#         form = LaptopForm(request.POST)
#         if form.is_valid():
#             laptop = form.save(commit=False)  # nu salva încă
#             laptop.nota_produs = 0  # Default - de exemplu 0
#             laptop.save()  # acum salvează
#             return redirect('admin_dashboard')
#     else:
#         form = LaptopForm()
#
#     return render(request, 'shop/adaugare_laptop.html', {'form': form})
#
#
# from django.shortcuts import render
# from .models import Laptop  # Numele modelului trebuie să corespundă cu cel din models.py
#
#
# def cautare_laptop(request):
#     laptopuri = None
#     marca = None
#
#     if request.method == 'POST':
#         marca = request.POST.get('marca', '').strip()
#         if marca:
#             # Căutăm atât în Brand cât și în Model
#             laptopuri = Laptop.objects.filter(brand__icontains=marca) | Laptop.objects.filter(
#                 model__icontains=marca)
#
#     return render(request, 'shop/cautare_laptop.html', {
#         'laptopuri': laptopuri,
#         'marca': marca
#     })
#
# from django.shortcuts import redirect, get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
# from .models import Laptop
#
# @csrf_exempt  # doar temporar, dacă nu funcționează cu tokenul CSRF, dar e mai bine să-l păstrezi în formular!
# def delete_laptop(request):
#     if request.method == "POST":
#         serial = request.POST.get("serielaptop")
#         laptop = get_object_or_404(Laptop, serielaptop=serial)
#         laptop.delete()
#         return redirect('/admin-dashboard/cautare_laptop/')
#     else:
#         return redirect('/admin-dashboard/cautare_laptop/')
#
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Laptop
#
# def edit_laptop(request, serielaptop):
#     laptop = get_object_or_404(Laptop, serielaptop=serielaptop)
#
#     if request.method == 'POST':
#         laptop.nume = request.POST.get('nume')
#         laptop.pret = request.POST.get('pret')
#         laptop.memorie_ram = request.POST.get('memorie_ram')
#         laptop.procesor = request.POST.get('procesor')
#         # Adaugă aici și alte câmpuri relevante
#
#         laptop.save()
#         return redirect('/admin-dashboard/cautare_laptop/')  # Redirect după salvare
#
#     return render(request, 'shop/edit-laptop.html', {'laptop': laptop})
#
# # shop/views.py
# from django.shortcuts import render, redirect
# from .forms import TabletaForm
#
# def adauga_tableta(request):
#     if request.method == 'POST':
#         form = TabletaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('adauga_tableta')  # sau pagina de listare
#     else:
#         form = TabletaForm()
#     return render(request, 'shop/adauga_tableta.html', {'form': form})
#
# from .models import Tableta
# def cautare_tableta(request):
#     tablete = None
#     marca = None
#
#     if request.method == 'POST':
#         marca = request.POST.get('marca', '').strip()
#         if marca:
#             # Căutăm atât în Brand cât și în Model
#             tablete = Tableta.objects.filter(Brand__icontains=marca) | Tableta.objects.filter(Model__icontains=marca)
#
#     return render(request, 'shop/cautare_tableta.html', {
#         'tablete': tablete,
#         'marca': marca
#     })
#
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Tableta
#
# def edit_tableta(request, serietableta):
#     tableta = get_object_or_404(Tableta, SerieTableta=serietableta)
#
#     if request.method == 'POST':
#         tableta.SistemOperare = request.POST.get('SistemOperare')
#         tableta.Brand = request.POST.get('Brand')
#         tableta.Model = request.POST.get('Model')
#         tableta.CapacitateRAM = request.POST.get('CapacitateRAM')
#         tableta.CapacitateMemorie = request.POST.get('CapacitateMemorie')
#         tableta.Culoare = request.POST.get('Culoare')
#         tableta.Lungime = request.POST.get('Lungime')
#         tableta.Latime = request.POST.get('Latime')
#         tableta.UnitatiMasura = request.POST.get('UnitatiMasura')
#         tableta.Grosime = request.POST.get('Grosime')
#         tableta.Greutate = request.POST.get('Greutate')
#         tableta.CapacitateAcumulator = request.POST.get('CapacitateAcumulator')
#         tableta.Rezolutie = request.POST.get('Rezolutie')
#         tableta.Diagonala = request.POST.get('Diagonala')
#         tableta.Conectivitate = request.POST.get('Conectivitate')
#         tableta.ModelProcesor = request.POST.get('ModelProcesor')
#         tableta.pret = request.POST.get('pret')
#         tableta.Disponibilitate = request.POST.get('Disponibilitate')
#         tableta.OptiuneLivrare = request.POST.get('OptiuneLivrare')
#
#         tableta.save()
#         return redirect('/admin-dashboard/cautare_tableta/')
#
#     return render(request, 'shop/edit_tableta.html', {'tableta': tableta})
#
# def delete_tableta(request):
#     if request.method == "POST":
#         serial = request.POST.get("SerieTableta")
#         tableta = get_object_or_404(Tableta, SerieTableta=serial)
#         tableta.delete()
#         return redirect('/admin-dashboard/cautare_tableta/')
#     else:
#         return redirect('/admin-dashboard/cautare_tableta/')
#
# def adaugare_telefon(request):
#     if request.method == 'POST':
#         form = TelefonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('adaugare_telefon')
#     else:
#         form = TelefonForm()
#     return render(request, 'shop/adaugare_telefon.html', {'form': form})
#
# from .models import Telefon
# def cautare_telefon(request):
#     telefon = None
#     marca = None
#
#     if request.method == 'POST':
#         marca = request.POST.get('marca', '').strip()
#         if marca:
#             # Căutăm atât în Brand cât și în Model
#             telefon = Telefon.objects.filter(Brand__icontains=marca) | Telefon.objects.filter(Model__icontains=marca)
#
#     return render(request, 'shop/cautare_telefon.html', {
#         'telefoane': telefon,
#         'marca': marca
#     })
#
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Telefon
#
# def editare_telefon(request, serie):
#     telefon = get_object_or_404(Telefon, SerieTelefon=serie)
#
#     if request.method == 'POST':
#         telefon.SistemOperare = request.POST['SistemOperare']
#         telefon.Brand = request.POST['Brand']
#         telefon.Model = request.POST['Model']
#         telefon.CapacitateRAM = request.POST['CapacitateRAM']
#         telefon.CapacitateMemorie = request.POST['CapacitateMemorie']
#         telefon.Culoare = request.POST['Culoare']
#         telefon.Lungime = request.POST['Lungime']
#         telefon.Latime = request.POST['Latime']
#         telefon.Grosime = request.POST['Grosime']
#         telefon.Diagonala = request.POST['Diagonala']
#         telefon.Greutate = request.POST['Greutate']
#         telefon.CapacitateAcumulator = request.POST['CapacitateAcumulator']
#         telefon.Material = request.POST['Material']
#         telefon.Rezolutie = request.POST['Rezolutie']
#         telefon.pret = request.POST['pret']
#         telefon.NotaProdus = request.POST.get('NotaProdus') or None
#         telefon.Disponibilitate = request.POST.get('Disponibilitate')
#         telefon.OptiuneLivrare = request.POST.get('OptiuneLivrare')
#         telefon.save()
#
#         return redirect('/admin-dashboard/cautare_telefon/')
#
#     return render(request, 'shop/edit_telefon.html', {
#         'telefon': telefon
#     })
#
# def delete_telefon(request):
#     if request.method == "POST":
#         serial = request.POST.get("SerieTelefon")
#         telefon = get_object_or_404(Telefon, SerieTelefon=serial)
#         telefon.delete()
#         return redirect('/admin-dashboard/cautare_telefon/')
#     else:
#         return redirect('/admin-dashboard/cautare_telefon/')
#
# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.db.models import Q
#
# def cauta_utilizatori(request):
#     query = request.GET.get('q', '')
#     utilizatori = []
#
#     if query:
#         utilizatori = User.objects.filter(
#             Q(username__icontains=query) |
#             Q(first_name__icontains=query) |
#             Q(last_name__icontains=query) |
#             Q(email__icontains=query)
#         )
#
#     context = {
#         'query': query,
#         'utilizatori': utilizatori
#     }
#     return render(request, 'shop/cautare_utilizatori.html', context)
#
# from django.shortcuts import get_object_or_404, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth.decorators import user_passes_test
# from django.urls import reverse
#
# @user_passes_test(lambda u: u.is_staff)  # Doar staff-ul poate șterge
# def sterge_utilizator(request, user_id):
#     utilizator = get_object_or_404(User, id=user_id)
#     if request.user == utilizator:
#         messages.error(request, "Nu poți șterge propriul cont.")
#     else:
#         utilizator.delete()
#         messages.success(request, f"Utilizatorul '{utilizator.username}' a fost șters cu succes.")
#     return redirect(reverse('cautare_utilizatori'))
#
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.models import User
# from django.urls import reverse
#
# def editare_utilizator(request, user_id):
#     utilizator = get_object_or_404(User, id=user_id)
#
#     if request.method == 'POST':
#         utilizator.first_name = request.POST.get('first_name')
#         utilizator.last_name = request.POST.get('last_name')
#         utilizator.email = request.POST.get('email')
#         utilizator.username = request.POST.get('username')
#         utilizator.is_staff = True if request.POST.get('is_staff') == 'on' else False
#         utilizator.is_active = True if request.POST.get('is_active') == 'on' else False
#         utilizator.save()
#         return redirect(reverse('cautare_utilizatori'))
#
#     return render(request, 'shop/editare_utilizator.html', {'utilizator': utilizator})
#
#
#
#
from django.shortcuts import render, get_object_or_404
from .models import Laptop
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User


# def index(request):
#     laptops = Laptop.objects.all()
#     context = {
#         'laptops': laptops
#     }
#     return render(request, 'shop/index.html', context)

# def index(request):
#     return render(request, 'shop/index.html')

from .models import Laptop

def index(request):
    laptops = Laptop.objects.all()
    return render(request, 'shop/index.html', {'laptops': laptops})

def product_detail(request, serielaptop):
    laptop = get_object_or_404(Laptop, serielaptop=serielaptop)
    context = {
        'laptop': laptop
    }
    return render(request, 'shop/product_detail.html', context)

def cart(request):
    # Pentru început, o pagină simplă, se poate extinde ca funcționalitate de coș.
    return render(request, 'shop/cart.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, TelefonForm, ComandaForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Nu salvăm încă în DB
            # Adăugăm câmpurile suplimentare
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            if form.cleaned_data.get('is_admin'):
                user.is_staff = True
            user.is_active = True  # În caz că vrei să gestionezi activarea manual
            user.save()

            messages.success(request, 'Contul a fost creat cu succes! Te poți loga acum.')
            return redirect('login')
        else:
            print("Erori formular:", form.errors)
            messages.error(request, 'Ceva nu a mers bine. Te rugăm să încerci din nou.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'shop/register.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser or user.is_staff:
                # Dacă este admin sau staff, redirecționează către pagina de admin
                return redirect('admin_dashboard')  # O pagină specială pentru admini
            else:
                # Dacă e utilizator normal
                return redirect('/')
        else:
            # Dacă username sau parola sunt greșite
            return render(request, 'shop/login.html', {'error': 'Utilizator sau parolă greșită'})

    return render(request, 'shop/login.html')

from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def admin_dashboard(request):
    return render(request, 'shop/admin_dashboard.html')

from django.shortcuts import render, redirect
from .forms import LaptopForm


def adaugare_laptop(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            laptop = form.save(commit=False)  # nu salva încă
            laptop.nota_produs = 0  # Default - de exemplu 0
            laptop.save()  # acum salvează
            return redirect('admin_dashboard')
    else:
        form = LaptopForm()

    return render(request, 'shop/adaugare_laptop.html', {'form': form})


from django.shortcuts import render
from .models import Laptop  # Numele modelului trebuie să corespundă cu cel din models.py


def cautare_laptop(request):
    laptopuri = None
    marca = None

    if request.method == 'POST':
        marca = request.POST.get('marca', '').strip()
        if marca:
            # Căutăm atât în Brand cât și în Model
            laptopuri = Laptop.objects.filter(brand__icontains=marca) | Laptop.objects.filter(
                model__icontains=marca)

    return render(request, 'shop/cautare_laptop.html', {
        'laptopuri': laptopuri,
        'marca': marca
    })

from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Laptop

@csrf_exempt  # doar temporar, dacă nu funcționează cu tokenul CSRF, dar e mai bine să-l păstrezi în formular!
def delete_laptop(request):
    if request.method == "POST":
        serial = request.POST.get("serielaptop")
        laptop = get_object_or_404(Laptop, serielaptop=serial)
        laptop.delete()
        return redirect('/admin-dashboard/cautare_laptop/')
    else:
        return redirect('/admin-dashboard/cautare_laptop/')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop

def edit_laptop(request, serielaptop):
    laptop = get_object_or_404(Laptop, serielaptop=serielaptop)

    if request.method == 'POST':
        laptop.nume = request.POST.get('nume')
        laptop.pret = request.POST.get('pret')
        laptop.memorie_ram = request.POST.get('memorie_ram')
        laptop.procesor = request.POST.get('procesor')
        # Adaugă aici și alte câmpuri relevante

        laptop.save()
        return redirect('/admin-dashboard/cautare_laptop/')  # Redirect după salvare

    return render(request, 'shop/edit-laptop.html', {'laptop': laptop})

# shop/views.py
from django.shortcuts import render, redirect
from .forms import TabletaForm

def adauga_tableta(request):
    if request.method == 'POST':
        form = TabletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adauga_tableta')  # sau pagina de listare
    else:
        form = TabletaForm()
    return render(request, 'shop/adauga_tableta.html', {'form': form})

from .models import Tableta
def cautare_tableta(request):
    tablete = None
    marca = None

    if request.method == 'POST':
        marca = request.POST.get('marca', '').strip()
        if marca:
            # Căutăm atât în Brand cât și în Model
            tablete = Tableta.objects.filter(Brand__icontains=marca) | Tableta.objects.filter(Model__icontains=marca)

    return render(request, 'shop/cautare_tableta.html', {
        'tablete': tablete,
        'marca': marca
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Tableta

def edit_tableta(request, serietableta):
    tableta = get_object_or_404(Tableta, SerieTableta=serietableta)

    if request.method == 'POST':
        tableta.SistemOperare = request.POST.get('SistemOperare')
        tableta.Brand = request.POST.get('Brand')
        tableta.Model = request.POST.get('Model')
        tableta.CapacitateRAM = request.POST.get('CapacitateRAM')
        tableta.CapacitateMemorie = request.POST.get('CapacitateMemorie')
        tableta.Culoare = request.POST.get('Culoare')
        tableta.Lungime = request.POST.get('Lungime')
        tableta.Latime = request.POST.get('Latime')
        tableta.UnitatiMasura = request.POST.get('UnitatiMasura')
        tableta.Grosime = request.POST.get('Grosime')
        tableta.Greutate = request.POST.get('Greutate')
        tableta.CapacitateAcumulator = request.POST.get('CapacitateAcumulator')
        tableta.Rezolutie = request.POST.get('Rezolutie')
        tableta.Diagonala = request.POST.get('Diagonala')
        tableta.Conectivitate = request.POST.get('Conectivitate')
        tableta.ModelProcesor = request.POST.get('ModelProcesor')
        tableta.pret = request.POST.get('pret')
        tableta.Disponibilitate = request.POST.get('Disponibilitate')
        tableta.OptiuneLivrare = request.POST.get('OptiuneLivrare')

        tableta.save()
        return redirect('/admin-dashboard/cautare_tableta/')

    return render(request, 'shop/edit_tableta.html', {'tableta': tableta})

def delete_tableta(request):
    if request.method == "POST":
        serial = request.POST.get("SerieTableta")
        tableta = get_object_or_404(Tableta, SerieTableta=serial)
        tableta.delete()
        return redirect('/admin-dashboard/cautare_tableta/')
    else:
        return redirect('/admin-dashboard/cautare_tableta/')

def adaugare_telefon(request):
    if request.method == 'POST':
        form = TelefonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adaugare_telefon')
    else:
        form = TelefonForm()
    return render(request, 'shop/adaugare_telefon.html', {'form': form})

from .models import Telefon
def cautare_telefon(request):
    telefon = None
    marca = None

    if request.method == 'POST':
        marca = request.POST.get('marca', '').strip()
        if marca:
            # Căutăm atât în Brand cât și în Model
            telefon = Telefon.objects.filter(Brand__icontains=marca) | Telefon.objects.filter(Model__icontains=marca)

    return render(request, 'shop/cautare_telefon.html', {
        'telefoane': telefon,
        'marca': marca
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Telefon

def editare_telefon(request, serie):
    telefon = get_object_or_404(Telefon, SerieTelefon=serie)

    if request.method == 'POST':
        telefon.SistemOperare = request.POST['SistemOperare']
        telefon.Brand = request.POST['Brand']
        telefon.Model = request.POST['Model']
        telefon.CapacitateRAM = request.POST['CapacitateRAM']
        telefon.CapacitateMemorie = request.POST['CapacitateMemorie']
        telefon.Culoare = request.POST['Culoare']
        telefon.Lungime = request.POST['Lungime']
        telefon.Latime = request.POST['Latime']
        telefon.Grosime = request.POST['Grosime']
        telefon.Diagonala = request.POST['Diagonala']
        telefon.Greutate = request.POST['Greutate']
        telefon.CapacitateAcumulator = request.POST['CapacitateAcumulator']
        telefon.Material = request.POST['Material']
        telefon.Rezolutie = request.POST['Rezolutie']
        telefon.pret = request.POST['pret']
        telefon.NotaProdus = request.POST.get('NotaProdus') or None
        telefon.Disponibilitate = request.POST.get('Disponibilitate')
        telefon.OptiuneLivrare = request.POST.get('OptiuneLivrare')
        telefon.save()

        return redirect('/admin-dashboard/cautare_telefon/')

    return render(request, 'shop/edit_telefon.html', {
        'telefon': telefon
    })

def delete_telefon(request):
    if request.method == "POST":
        serial = request.POST.get("SerieTelefon")
        telefon = get_object_or_404(Telefon, SerieTelefon=serial)
        telefon.delete()
        return redirect('/admin-dashboard/cautare_telefon/')
    else:
        return redirect('/admin-dashboard/cautare_telefon/')

from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q

def cauta_utilizatori(request):
    query = request.GET.get('q', '')
    utilizatori = []

    if query:
        utilizatori = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )

    context = {
        'query': query,
        'utilizatori': utilizatori
    }
    return render(request, 'shop/cautare_utilizatori.html', context)

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

@user_passes_test(lambda u: u.is_staff)  # Doar staff-ul poate șterge
def sterge_utilizator(request, user_id):
    utilizator = get_object_or_404(User, id=user_id)
    if request.user == utilizator:
        messages.error(request, "Nu poți șterge propriul cont.")
    else:
        utilizator.delete()
        messages.success(request, f"Utilizatorul '{utilizator.username}' a fost șters cu succes.")
    return redirect(reverse('cautare_utilizatori'))

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse

def editare_utilizator(request, user_id):
    utilizator = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        utilizator.first_name = request.POST.get('first_name')
        utilizator.last_name = request.POST.get('last_name')
        utilizator.email = request.POST.get('email')
        utilizator.username = request.POST.get('username')
        utilizator.is_staff = True if request.POST.get('is_staff') == 'on' else False
        utilizator.is_active = True if request.POST.get('is_active') == 'on' else False
        utilizator.save()
        return redirect(reverse('cautare_utilizatori'))

    return render(request, 'shop/editare_utilizator.html', {'utilizator': utilizator})

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecționează spre pagina principală
        elif user.is_superuser:
            return redirect('/admin/')
        elif not user.is_superuser:
            return redirect('index')  # numele rutei pentru magazin
        else:
            return render(request, 'shop/login.html', {'error': 'Date invalide'})
    return render(request, 'shop/login.html')

from django.shortcuts import render
from .models import Laptop

def lista_laptopuri(request):
    laptopuri = Laptop.objects.all()
    return render(request, 'shop/laptopuri.html', {'laptopuri': laptopuri})

from django.shortcuts import render, get_object_or_404
from .models import Laptop

def detalii_laptop(request, serielaptop):
    laptop = get_object_or_404(Laptop, serielaptop=serielaptop)
    return render(request, 'shop/detalii_laptop.html', {'laptop': laptop})

def lista_tablete(request):
    tablete = Tableta.objects.all()
    return render(request, 'shop/tablete.html', {'tablete': tablete})

from django.shortcuts import render, get_object_or_404
from .models import Laptop

from .models import Tableta

def detalii_tableta(request, serietableta):
    tableta = get_object_or_404(Tableta, SerieTableta=serietableta)
    return render(request, 'shop/detalii_tableta.html', {'tableta': tableta})


from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'shop/login.html'

    def get_success_url(self):
        if self.request.user.is_staff:
            return '/admin/'  # adminii merg în admin
        return '/'  # user normal merge în index

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def user_profile(request):
    return render(request, 'shop/user_profile.html', {'user': request.user})

from django.shortcuts import render, get_object_or_404
from .models import Telefon

def lista_telefoane(request):
    telefoane = Telefon.objects.all()
    return render(request, "shop/telefoane.html", {"telefoane": telefoane})

def detalii_telefon(request, serie):
    telefon = get_object_or_404(Telefon, SerieTelefon=serie)
    return render(request, "shop/detalii_telefon.html", {"telefon": telefon})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Laptop, Telefon, Tableta

@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_type, product_id):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product_type=product_type,
        product_id=product_id
    )
    if not created:
        item.quantity += 1
        item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('view_cart')


from django.shortcuts import render
from .models import Order  # asigură-te că modelul Order e importat

def cauta_comenzi_dupa_user(request):
    comenzi = []
    user_id = request.GET.get('user_id')

    if user_id:
        comenzi = Order.objects.filter(user_id=user_id)

    return render(request, 'shop/cautare_comenzi.html', {
        'comenzi': comenzi,
        'user_id': user_id
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm  # va trebui să-l creezi

def update_comanda(request, pk):
    comanda = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        form = ComandaForm(request.POST, instance=comanda)
        if form.is_valid():
            form.save()
            return redirect('cauta_comenzi_dupa_user')
    else:
        form = ComandaForm(instance=comanda)

    return render(request, 'shop/update_comanda.html', {'form': form})

def delete_comanda(request, pk):
    comanda = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        comanda.delete()
        return redirect('cauta_comenzi_dupa_user')  # redirecționează după ștergere

    return render(request, 'shop/confirm_delete.html', {'comanda': comanda})

