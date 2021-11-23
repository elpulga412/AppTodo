from django.contrib import admin
from .models import *

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'createAt')

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Photo, PhotoAdmin)