from django.contrib import admin
from .models import Post # se importa el modelo Post

# Register your models here.
admin.site.register(Post) # se registra el modelo Post para hacerlo visible en la página del administrador
