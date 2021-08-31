from django.contrib import admin

from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'gender', 'age', 'food', 'notes')
    list_filter = ('type', 'gender', 'food')
