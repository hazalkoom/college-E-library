from django.contrib import admin
from .models import Subject, Books, Lectures


# Register your models here.

admin.site.register(Subject)
admin.site.register(Books)
admin.site.register(Lectures)
