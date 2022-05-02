from django.core.management.base import BaseCommand
from covid_data.models import CovidData
import requests


def get_data():
    response = requests.get('https://disease.sh/v3/covid-19/countries')

    country = response.json()
    for c in country:
        country = CovidData(
            country=c["country"],
            country_code=c["countryInfo"]["iso2"],
            total_cases=c["cases"],
            total_deaths=c["deaths"],
            total_recovered=c["recovered"]
        )
        country.save()
        print(country)


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_data()
        print("completed")

# invoke this script by running the command ./manage.py populate_db
# source https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database