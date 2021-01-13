from django.contrib import admin

# Register your models here.
from .models import class_routine
from .models import Syllabus
from .models import Employment

admin.site.register(class_routine)
admin.site.register(Syllabus)
admin.site.register(Employment)