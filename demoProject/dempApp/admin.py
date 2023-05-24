from django.contrib import admin
from .models import catalog
from .models import detail
# Register your models here.
admin.site.register(catalog)
admin.site.register(detail)