from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
'''en vez de utilizar http response utilizamos un 
return con render, que viene con django por defecto
registro.html no lo reconoce hasta que no incluyo la aplicacion dentro del settings.py'''
'''def registro(request):
    return render(request, "registro.html")'''


def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, F"Bienvenide de nuevo {nombre_usuario}")
                return redirect("blog")
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")
    form = AuthenticationForm()
    return render(request, "acceder.html", {"form": form})


class VistaRegistro(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        # este UserCreationForm esta directamente conectado con el auth_user de la bbdd
        form = UserCreationForm()
        return render(request, "registro.html", {"form": form})

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre = form.cleaned_data.get("username")
            messages.success(request, f"Bienvenide a la plataforma {nombre}")
            login(request, usuario)
            return redirect("blog")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro.html", {"form": form})


def salir(request):
    logout(request)
    messages.success(request, f"Tu sesión se ha cerrado correctamente")
    return redirect("acceder")
