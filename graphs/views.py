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

def save_data(request):
    source = request.GET.get('source')
    climates = request.GET.getlist('climates[]')
    student_id = request.GET.get('student_id')

    years = GraphData.objects.filter(student=student_id)
    first_year = years.filter(graph_year=climates[0])
    second_year = years.filter(graph_year=climates[4])
    third_year = years.filter(graph_year=climates[8])

    first_year.update(average_temperature=climates[1], average_precipitation=climates[2], event=climates[3], latitude=climates[12], longitude=climates[13], source_text=source)
    second_year.update(average_temperature=climates[5], average_precipitation=climates[6], event=climates[7], latitude=climates[12], longitude=climates[13], source_text=source)
    third_year.update(average_temperature=climates[9], average_precipitation=climates[10], event=climates[11], latitude=climates[12], longitude=climates[13], source_text=source)

    return render(request, 'graphs/add_data.html')

def load_years(request):
    student_id = request.GET.get('student')
    years = GraphData.objects.filter(student=student_id).order_by('graph_year')

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

        return Response(data)
