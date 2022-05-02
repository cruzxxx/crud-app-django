from django.contrib import admin
from .models import CovidData


class CovidDataAdmin(admin.ModelAdmin):
    list_display = (
        'country',
        'total_cases',
        'total_deaths',
        'total_recovered'
    )


admin.site.register(CovidData, CovidDataAdmin)