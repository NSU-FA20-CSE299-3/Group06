from django.contrib import admin

# Register your models here.
from .models import Class_routine
from .models import Syllabus
from .models import Employment
from .models import About

admin.site.register(Class_routine)
admin.site.register(Syllabus)
admin.site.register(Employment)
admin.site.register(About)