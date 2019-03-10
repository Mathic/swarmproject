from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GraphData

# Create your views here.
def index(request):
    return render(request, 'graphs/index.html')


class ClimateData(APIView):
    authentication_classes=[]
    permission_classes=[]

    def get(self, request, format=None):
        temperatures = dict()
        for climate in GraphData.objects.all():
            print(climate.graph_year)
            temperatures[climate.graph_year] = climate.average_temperature

        temperatures = sorted(temperatures.items(), key=lambda x: x[1])
        temperatures = dict(temperatures)

        print("keys %s"%(temperatures.keys()))
        data = {
            "climate_labels": temperatures.keys(),
            "climate_data": temperatures.values()
        }

        return Response(data)
