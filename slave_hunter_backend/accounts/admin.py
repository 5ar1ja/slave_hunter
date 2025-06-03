from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'city', 'email')
    search_fields = ('name', 'city', 'email')
    list_filter = ('city',)

# Если не используешь декоратор:
# admin.site.register(Company, CompanyAdmin)
