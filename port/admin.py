from django.contrib import admin
from .models import Member, Proyects, Friends, Proyect_Finder

# Register your models here.

admin.site.register(Member)
admin.site.register(Proyect_Finder)
admin.site.register(Friends)
admin.site.register(Proyects)

