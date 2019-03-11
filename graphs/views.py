from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GraphData, Student

# Create your views here.
def index(request):
    return render(request, 'graphs/index.html')

def add_data(request):
    names = Student.objects.all()
    form = request.POST

    return render(request, 'graphs/add_data.html', {'names': names})

def load_years(request):
    student_id = request.GET.get('student')
    years = GraphData.objects.filter(student=student_id).order_by('graph_year')
    print(years[0].source_text)
    return render(request, 'graphs/year_options.html', {'years': years, 'source': years[0]})

class ClimateData(APIView):
    authentication_classes=[]
    permission_classes=[]

    def get(self, request, format=None):
        years = []
        temperaturesOttawa = []
        precipitationOttawa = []
        temperaturesVictoria = []
        precipitationVictoria = [ ]

        climates = GraphData.objects.order_by('graph_year')
        for climate in climates:
            if climate.graph_year not in years:
                years.append(climate.graph_year)
            if (climate.source_text == "Ottawa CDA"):
                temperaturesOttawa.append(climate.average_temperature)
                precipitationOttawa.append(climate.average_precipitation)
            else:
                temperaturesVictoria.append(climate.average_temperature)
                precipitationVictoria.append(climate.average_precipitation)

        data = {
            "climate_labels": years,
            "climate_data1": temperaturesOttawa,
            "climate_data2": precipitationOttawa,
            "climate_data3": temperaturesVictoria,
            "climate_data4": precipitationVictoria
        }

        print("climates: %s \ntemp: %s \nprec: %s"% (climates, temperaturesOttawa, precipitationOttawa))
        return Response(data)
