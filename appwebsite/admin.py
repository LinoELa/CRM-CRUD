from django.contrib import admin

# Importamo el modelo 
from .models import Record

# Registramos nuestros modelo s

admin.site.register(Record)

