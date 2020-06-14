from django.contrib import admin

from .models import bill

@admin.register(bill)
class billAdmin(admin.ModelAdmin):
    list_display = ["NMI","serial","readingValue","date","fileName"]
    search_fields = ("NMI","serial")