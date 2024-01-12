from django.contrib import admin
from .models import Articles,Publisher, Reporter

# Register your models here.
admin.site.register(Articles)
admin.site.register(Publisher)
admin.site.register(Reporter)