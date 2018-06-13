from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created']
    search_fields = ['name', 'email']
    list_filter = ['created']

admin.site.register(Message, MessageAdmin)
