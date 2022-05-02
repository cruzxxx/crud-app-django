from django.shortcuts import render
from .models import CovidData
import requests


def get_covid_data(request):
    all_covid_data = {}
    if 'country' in request.GET:
        country = request.GET['country']
        url = f'https://disease.sh/v3/covid-19/countries/{country}'
        response = requests.get(url)
        data = response.json()
        covid_data = data['meals']

        for i in covid_data:
            covid_data = CovidData(
                country=i['country'],
                total_cases=i['cases'],
                total_deaths=i['deaths'],
                total_recovered=i['recovered'],
            )
            covid_data.save()
            covid_data = CovidData.objects.all().order_by('-id')

    return render(request, {"all_covid_data": all_covid_data})
