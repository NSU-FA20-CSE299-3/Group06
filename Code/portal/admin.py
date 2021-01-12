from django.contrib import admin

# Register your models here.
from .models import Academic
from .models import Syllabus
from .models import Employment

admin.site.register(Academic)
admin.site.register(Syllabus)
admin.site.register(Employment)