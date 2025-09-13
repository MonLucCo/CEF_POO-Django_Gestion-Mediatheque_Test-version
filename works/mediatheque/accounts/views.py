from django.shortcuts import render

def accueil(request):
    return render(request, 'accounts/accueil.html')
