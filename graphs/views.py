from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GraphData, Student, Month

# test method to create month for each year
def test(request):
    twelve = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    years = GraphData.objects.order_by('graph_year')

    for y in years:
        months = y.month_set.all()
        for t in twelve:
            if months.filter(month=t).first() == None:
                month_instance = Month.objects.create(month=t, year=y)
                print(month_instance)

    return render(request, 'graphs/test.html')

def index(request):
    return render(request, 'graphs/index.html', {'nbar': 'graph'})

def data(request):
    ottawa = GraphData.objects.filter(source_text='Ottawa CDA').order_by('graph_year')
    victoria = GraphData.objects.filter(source_text='Victoria Gonzales').order_by('graph_year')

    return render(request, 'graphs/data.html', {'ottawa': ottawa, 'victoria': victoria, 'nbar': 'data'})

def data_m(request):
    years = GraphData.objects.all()

    return render(request, 'graphs/data_m.html', {'years': years, 'nbar': 'data'})

def load_months(request):
    year_id = request.GET.get('yearId')
    months = Month.objects.filter(year=year_id)

    return render(request, 'graphs/month_options.html', {'months': months})

def add_data(request):
    names = Student.objects.all()
    form = request.POST

    return render(request, 'graphs/add_data.html', {'names': names, 'nbar': 'add'})

def load_years(request):
    student_id = request.GET.get('student')
    years = GraphData.objects.filter(student=student_id).order_by('graph_year')

    return render(request, 'graphs/year_options.html', {'years': years, 'source': years[0]})

def save_data(request):
    student_id = request.GET.get('student_id')
    climates = request.GET.getlist('climates[]')
    source = request.GET.get('source')
    temps = list(request.GET.getlist('temps[]'))
    precips = list(request.GET.getlist('precips[]'))

    years = GraphData.objects.filter(student=student_id)
    first_year = years.filter(graph_year=climates[0])
    second_year = years.filter(graph_year=climates[4])
    third_year = years.filter(graph_year=climates[8])

    first_months = Month.objects.filter(year=first_year)
    temp1 = temps[0].split() + temps[1].split() + temps[2].split()
    precip1 = precips[0].split() + precips[1].split() + precips[2].split()

    i = 0

    for y in years:
        months = y.month_set.all()
        for m in months:
            this_month = Month.objects.filter(year=y, month=m)
            this_temp = float(this_month.values_list('total_temperature', flat=True)[0])
            this_precip = float(this_month.values_list('total_precipitation', flat=True)[0])
            if (this_temp - float(temp1[i])) != 0.0:
                this_month.update(total_temperature=float(temp1[i]))
                print(this_month.values_list('total_temperature', flat=True)[0])
            if (this_precip - float(precip1[i])) != 0.0:
                this_month.update(total_precipitation=float(precip1[i]))
                print(float(this_month.values_list('total_precipitation', flat=True)[0]) - float(precip1[i]))
                print(float(precip1[i]))
            i += 1

    first_year.update(average_temperature=climates[1], average_precipitation=climates[2], event=climates[3], latitude=climates[12], longitude=climates[13], source_text=source)
    second_year.update(average_temperature=climates[5], average_precipitation=climates[6], event=climates[7], latitude=climates[12], longitude=climates[13], source_text=source)
    third_year.update(average_temperature=climates[9], average_precipitation=climates[10], event=climates[11], latitude=climates[12], longitude=climates[13], source_text=source)

    return render(request, 'graphs/add_data.html')

class ClimateData(APIView):
    authentication_classes=[]
    permission_classes=[]

    def get(self, request, format=None):
        years = []
        temperaturesOttawa = []
        precipitationOttawa = []
        temperaturesVictoria = []
        precipitationVictoria = []

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
