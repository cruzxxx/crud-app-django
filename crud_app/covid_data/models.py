from django.db import models


class CovidData(models.Model):
    country = models.CharField(max_length=1000, blank=True, null=True)
    country_code = models.CharField(max_length=2000, blank=True, null=True)
    total_cases = models.CharField(max_length=2000, blank=True, null=True)
    total_deaths = models.CharField(max_length=2000, blank=True, null=True)
    total_recovered = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.country
