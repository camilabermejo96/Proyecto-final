from django.contrib import admin
from blog.models import Autor, Libro, Editorial,Avatar

# Register your models here.
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Avatar)
