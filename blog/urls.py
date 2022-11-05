from django.contrib import admin
from django.urls import path, include
from blog.views import (
    mostrar_inicio,
    procesar_formulario,
    procesar_formulario_libro,
    procesar_formulario_editorial,
    busqueda,
    buscar,
    busqueda_libro,
    buscar_libro,
    busqueda_editorial,
    buscar_editorial,
    AutorList,
    LibroList,
    EditorialList,
    AutorCreacion,
    AutorDelete,
    AutorDetalle,
    AutorUpdateView,
    LibroCreacion,
    LibroDelete,
    LibroDetalle,
    LibroUpdateView,
    EditorialCreacion,
    EditorialDelete,
    EditorialDetalle,
    EditorialUpdateView,
    MyLogin,
    MyLogout,
    register,
    editar_perfil,
    agregar_avatar,
)

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario/", procesar_formulario, name="formulario"),  # Para agregar autores
    path(
        "formulario-libro/", procesar_formulario_libro, name="formulario_libro"
    ),  # Para agregar libros
    path(
        "formulario-editorial/",
        procesar_formulario_editorial,
        name="formulario_editorial",
    ),  # Para agregar editoriales
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar),  # Para buscar autores
    path("busqueda-libro/", busqueda_libro, name="busqueda_libro"),
    path("buscar-libro", buscar_libro),
    path("busqueda-editorial/", busqueda_editorial, name="busqueda_editorial"),
    path("buscar-editorial/", buscar_editorial),
    path("autor-lista", AutorList.as_view(), name="autor-lista"),
    path("libro-lista", LibroList.as_view(), name="libro-lista"),
    path("editorial-lista", EditorialList.as_view(), name="editorial-lista"),
    path("r'(?P<pk>\d+)^$'", AutorDetalle.as_view(), name="AutorDetail"),
    path("autor-nuevo/", AutorCreacion.as_view(), name="AutorNew"),
    path("editar/<pk>", AutorUpdateView.as_view(), name="AutorUpdate"),
    path("borrar/<pk>", AutorDelete.as_view(), name="AutorDelete"),
    path("libro/detalle/<pk>", LibroDetalle.as_view(), name="LibroDetail"),
    path("libro-nuevo/", LibroCreacion.as_view(), name="LibroNew"),
    path("editar-libro/<pk>", LibroUpdateView.as_view(), name="LibroUpdate"),
    path("borrar-libro/<pk>", LibroDelete.as_view(), name="LibroDelete"),
    path("editorial/detalle/<pk>", EditorialDetalle.as_view(), name="EditorialDetail"),
    path("editorial-nuevo/", EditorialCreacion.as_view(), name="EditorialNew"),
    path(
        "editar-editorial/<pk>", EditorialUpdateView.as_view(), name="EditorialUpdate"
    ),
    path("borrar-editorial/<pk>", EditorialDelete.as_view(), name="EditorialDelete"),
    path("inicio/", mostrar_inicio, name="Inicio"),
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("register/", register, name="Register"),
    path("editar-perfil/", editar_perfil, name="EditarPerfil"),
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),

]
