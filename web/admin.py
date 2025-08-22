# web/admin.py
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'submitted_at')
    search_fields = ('name', 'email', 'message')