from django.contrib import admin
from .models import Inspection
from .models import Condition
# Register your models here.
admin.site.register(Inspection)
admin.site.register(Condition)