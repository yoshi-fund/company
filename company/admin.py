from django.contrib import admin
from .models import Company

class Search(admin.ModelAdmin):
    
    search_fields = ['会社名']

admin.site.register(Company, Search)

# Register your models here.
