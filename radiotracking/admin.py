from django.contrib import admin

# Register your models here.
from radiotracking.models import Program, Station

admin.site.register(Program)
admin.site.register(Station)
