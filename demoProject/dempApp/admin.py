from django.contrib import admin
from .models import catalog
from .models import detail
from .models import quote
# Register your models here.
admin.site.register(catalog)
admin.site.register(detail)
admin.site.register(quote)