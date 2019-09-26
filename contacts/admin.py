from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'contact_date')
    list_display_links = ('name', 'email')
    search_fields = ('name', 'email', 'message')
    list_per_page = 10

admin.site.register(Contact, ContactAdmin)

