from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(GraphData)
admin.site.register(Month)
admin.site.register(YearlyAverage)
admin.site.register(MonthlyAverage)
