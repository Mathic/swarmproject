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
    return render(request, 'graphs/index.html', {'nbar': 'yearly_graph'})

def monthly_graph(request):
    return render(request, 'graphs/monthly_graph.html', {'nbar': 'monthly_graph'})

def data(request):
    ottawa = GraphData.objects.filter(source_text='Ottawa CDA').order_by('graph_year')
    victoria = GraphData.objects.filter(source_text='Victoria Gonzales').order_by('graph_year')

    return render(request, 'graphs/data.html', {'ottawa': ottawa, 'victoria': victoria, 'nbar': 'data'})

def data_m(request):
    years = GraphData.objects.order_by('graph_year').values_list('graph_year', flat=True).distinct()

    return render(request, 'graphs/data_m.html', {'years': years, 'nbar': 'data'})

def load_months(request):
    ottawa = []
    victoria = []
    year = request.GET.get('year')
    years = GraphData.objects.filter(graph_year=year)
    # print(years)
    # months = Month.objects.filter(year=year_id)
    for y in years:
        if y.source_text == 'Ottawa CDA':
            ottawa = Month.objects.filter(year=y.id)
        else:
            victoria = Month.objects.filter(year=y.id)

    print(ottawa)

    return render(request, 'graphs/month_options.html', {'ottawa': ottawa, 'victoria': victoria})

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

    def get(self, request, format=None):
        climates = GraphData.objects.order_by('graph_year')
        years = climates.values_list('graph_year', flat=True).distinct()
        temperaturesOttawa = []
        precipitationOttawa = []
        temperaturesVictoria = []
        precipitationVictoria = []
        tempDiffOttawa = []
        tempDiffVictoria = []

        i = j = avgTotalTempVictoria = avgTotalTempOttawa = 0

        for climate in climates:
            if (climate.source_text == "Ottawa CDA"):
                temperaturesOttawa.append(climate.average_temperature)
                precipitationOttawa.append(climate.average_precipitation)
                if climate.average_temperature != 0:
                    i += 1
            else:
                temperaturesVictoria.append(climate.average_temperature)
                precipitationVictoria.append(climate.average_precipitation)
                if climate.average_temperature != 0:
                    j += 1

        if i != 0:
            avgTotalTempOttawa = sum(temperaturesOttawa[0:len(temperaturesOttawa)])/i
            print(avgTotalTempOttawa)
        if j != 0:
            avgTotalTempVictoria = sum(temperaturesVictoria[0:len(temperaturesVictoria)])/j
            print(avgTotalTempVictoria)

        for k in range(len(temperaturesOttawa)):
            tempDiffOttawa.append(temperaturesOttawa[k] - avgTotalTempOttawa)

        for k in range(len(temperaturesVictoria)):
            tempDiffVictoria.append(temperaturesVictoria[k] - avgTotalTempVictoria)

        print(tempDiffOttawa)

        data = {
            "climate_labels": years,
            "climate_data1": tempDiffOttawa,
            "climate_data2": precipitationOttawa,
            "climate_data3": tempDiffVictoria,
            "climate_data4": precipitationVictoria
        }

        return Response(data)

class MonthlyData(APIView):

    def get(self, request, format=None):
        months = Month.objects.all()
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        i = j = 0
        omonths = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        vmonths = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        omonths_p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        vmonths_p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for m in months:
            if (m.year.source_text == "Ottawa CDA"):
                # print("%s %s %s"% (m.month, m.total_temperature, month_names[0]))
                if (m.month == month_names[0]):
                    omonths[0] += m.total_temperature
                    omonths_p[0] += m.total_precipitation
                    i += 1
                if (m.month == month_names[1]):
                    omonths[1] += m.total_temperature
                    omonths_p[1] += m.total_precipitation
                if (m.month == month_names[2]):
                    omonths[2] += m.total_temperature
                    omonths_p[2] += m.total_precipitation
                if (m.month == month_names[3]):
                    omonths[3] += m.total_temperature
                    omonths_p[3] += m.total_precipitation
                if (m.month == month_names[4]):
                    omonths[4] += m.total_temperature
                    omonths_p[4] += m.total_precipitation
                if (m.month == month_names[5]):
                    omonths[5] += m.total_temperature
                    omonths_p[5] += m.total_precipitation
                if (m.month == month_names[6]):
                    omonths[6] += m.total_temperature
                    omonths_p[6] += m.total_precipitation
                if (m.month == month_names[7]):
                    omonths[7] += m.total_temperature
                    omonths_p[7] += m.total_precipitation
                if (m.month == month_names[8]):
                    omonths[8] += m.total_temperature
                    omonths_p[8] += m.total_precipitation
                if (m.month == month_names[9]):
                    omonths[9] += m.total_temperature
                    omonths_p[9] += m.total_precipitation
                if (m.month == month_names[10]):
                    omonths[10] += m.total_temperature
                    omonths_p[10] += m.total_precipitation
                if (m.month == month_names[11]):
                    omonths[11] += m.total_temperature
                    omonths_p[11] += m.total_precipitation
            else:
                if (m.month == month_names[0]):
                    vmonths[0] += m.total_temperature
                    j += 1
                if (m.month == month_names[1]):
                    vmonths[1] += m.total_temperature
                    vmonths_p[1] += m.total_precipitation
                if (m.month == month_names[2]):
                    vmonths[2] += m.total_temperature
                    vmonths_p[2] += m.total_precipitation
                if (m.month == month_names[3]):
                    vmonths[3] += m.total_temperature
                    vmonths_p[3] += m.total_precipitation
                if (m.month == month_names[4]):
                    vmonths[4] += m.total_temperature
                    vmonths_p[4] += m.total_precipitation
                if (m.month == month_names[5]):
                    vmonths[5] += m.total_temperature
                    vmonths_p[5] += m.total_precipitation
                if (m.month == month_names[6]):
                    vmonths[6] += m.total_temperature
                    vmonths_p[6] += m.total_precipitation
                if (m.month == month_names[7]):
                    vmonths[7] += m.total_temperature
                    vmonths_p[7] += m.total_precipitation
                if (m.month == month_names[8]):
                    vmonths[8] += m.total_temperature
                    vmonths_p[8] += m.total_precipitation
                if (m.month == month_names[9]):
                    vmonths[9] += m.total_temperature
                    vmonths_p[9] += m.total_precipitation
                if (m.month == month_names[10]):
                    vmonths[10] += m.total_temperature
                    vmonths_p[10] += m.total_precipitation
                if (m.month == month_names[11]):
                    vmonths[11] += m.total_temperature
                    vmonths_p[11] += m.total_precipitation

        for k in range(len(omonths)):
            omonths[k] = omonths[k]/i
            omonths_p[k] = omonths_p[k]/i

        for k in range(len(vmonths)):
            vmonths[k] = vmonths[k]/j
            vmonths_p[k] = vmonths_p[k]/j

        print(omonths)
        print(vmonths)

        data = {
            'month_names': month_names,
            'vmonths': vmonths,
            'omonths': omonths,
            'vmonths_p': vmonths_p,
            'omonths_p': omonths_p,
        }
        return Response(data)
