from http.client import HTTPResponse
from django.shortcuts import render
from blog.models import Autor, Libro, Editorial
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from blog.forms import AvatarForm, UserEditionForm
from blog.models import Avatar
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "blog/formulario.html")

    autor = Autor(nombre=request.POST["nombre"], apellido=request.POST["apellido"])
    autor.save()
    return render(request, "blog/inicio.html")


def procesar_formulario_libro(request):
    if request.method != "POST":
        return render(request, "blog/formulario-libro.html")

    libro = Libro(
        titulo=request.POST["titulo"],
        genero=request.POST["genero"],
        publicacion=request.POST["publicacion"],
    )
    libro.save()
    return render(request, "blog/inicio.html")


def procesar_formulario_editorial(request):
    if request.method != "POST":
        return render(request, "blog/formulario-editorial.html")

    editorial = Editorial(nombre=request.POST["nombre"])
    editorial.save()
    return render(request, "blog/inicio.html")


@login_required
def busqueda(request):
    return render(request, "blog/busqueda.html")


@login_required
def buscar(request):

    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        autores = Autor.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "autores_encontrados": autores}

        return render(request, "blog/resultado_busqueda.html", contexto)


@login_required
def busqueda_libro(request):
    return render(request, "blog/busqueda-libro.html")


@login_required
def buscar_libro(request):

    if not request.GET["titulo"]:
        return HttpResponse("No enviaste datos")
    else:
        titulo_a_buscar = request.GET["titulo"]
        libros = Libro.objects.filter(titulo=titulo_a_buscar)

        contexto = {"titulo": titulo_a_buscar, "libros_encontrados": libros}

        return render(request, "blog/resultado_busqueda_libro.html", contexto)


@login_required
def busqueda_editorial(request):
    return render(request, "blog/busqueda-editorial.html")


@login_required
def buscar_editorial(request):

    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        editoriales = Editorial.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "editoriales_encontrados": editoriales}

        return render(request, "blog/resultado_busqueda_editorial.html", contexto)


class AutorList(LoginRequiredMixin, ListView):
    model = Autor
    template_name = "blog/autores_list.html"


class LibroList(LoginRequiredMixin, ListView):
    model = Libro
    template_name = "blog/libros_list.html"


class EditorialList(LoginRequiredMixin, ListView):
    model = Editorial
    template_name = "blog/editoriales_list.html"


######################################################################################
class AutorDetalle(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "blog/autor_detalle.html"


class AutorCreacion(LoginRequiredMixin, CreateView):
    model = Autor
    fields = ["nombre", "apellido"]
    success_url = "/blog/autor-lista"


class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    success_url = "/blog/autor-lista"
    fields = ["nombre", "apellido"]


class AutorDelete(LoginRequiredMixin, DeleteView):

    model = Autor
    success_url = "/blog/autor-lista"


class LibroDetalle(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = "blog/libro_detalle.html"


class LibroCreacion(LoginRequiredMixin, CreateView):
    model = Libro
    fields = ["titulo", "genero"]
    success_url = "/blog/libro-lista"


class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    success_url = "/blog/libro-lista"
    fields = ["titulo", "genero"]


class LibroDelete(LoginRequiredMixin, DeleteView):

    model = Libro
    success_url = "/blog/libro-lista"


class EditorialDetalle(LoginRequiredMixin, DetailView):
    model = Editorial
    template_name = "blog/editorial_detalle.html"


class EditorialCreacion(LoginRequiredMixin, CreateView):
    model = Editorial
    fields = ["nombre"]
    success_url = "/blog/editorial-lista"


class EditorialUpdateView(LoginRequiredMixin, UpdateView):
    model = Editorial
    success_url = "/blog/editorial-lista"
    fields = ["nombre"]


class EditorialDelete(LoginRequiredMixin, DeleteView):

    model = Editorial
    success_url = "/blog/editorial-lista"


class MyLogin(LoginView):
    template_name = "blog/login.html"


class MyLogout(LogoutView, LoginRequiredMixin):
    template_name = "blog/logout.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "blog/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "blog/registro.html", {"form": form})


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "blog/inicio.html", {"avatar": avatar.imagen.url})

    contexto = {
        "user": user,
        "form": form,
        
    }
    return render(request, "blog/editarPerfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "blog/inicio.html")

    contexto = {"form": form}
    return render(request, "blog/avatar_form.html", contexto)
