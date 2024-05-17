from django.contrib import admin
from .models import ZodiacSign, Professions, FamousPerson, User

admin.site.register(User)
admin.site.register(ZodiacSign)
admin.site.register(Professions)
admin.site.register(FamousPerson)
