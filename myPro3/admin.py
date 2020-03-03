from django.contrib import admin

# Register your models here.
from .models import allowed,song
admin.site.register(allowed)
admin.site.register(song)
