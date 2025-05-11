from django.contrib import admin
from .models import Products, Contact_Form

admin.site.register(Products)

@admin.register(Contact_Form)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('email',)
