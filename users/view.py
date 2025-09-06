from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profil_utilizator(request):
    user = request.user
    # Dacă vrei să adaugi comenzile, le vei extrage aici din modelul comenzilor (dacă ai unul)
    comenzi = []  # Exemplu gol pentru acum
    return render(request, 'users/profil.html', {'user': user, 'comenzi': comenzi})
