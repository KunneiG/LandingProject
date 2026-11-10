from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ('title',)}  # Автозаполнение слага