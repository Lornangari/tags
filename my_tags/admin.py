from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, Editor
# Register your models here.
admin.site.register(Blog)
admin.site.register(Editor)
