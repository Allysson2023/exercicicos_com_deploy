from django.shortcuts import render

# Create your views here.
def perfil(request):
    return render (
        request, 
        'contact/perfil.html',
    )