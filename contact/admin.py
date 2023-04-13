from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone" "email", "message", 'created_date']
    date_hierarchy = 'created_date'


admin.site.register(Contact)
