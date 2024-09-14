from django.contrib import admin

from .models import Criterion, Lesson, Grade


admin.site.register(Criterion)
admin.site.register(Lesson)
admin.site.register(Grade)