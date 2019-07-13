from django.contrib import admin
from .models import FibNumber


@admin.register(FibNumber)
class FibNumberAdmin(admin.ModelAdmin):
    pass
