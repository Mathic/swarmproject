from django.urls import path

from . import views

urlpatterns = [
    path('api/chart/data', views.ClimateData.as_view(), name='api-chart-data'),
    path('', views.index, name='index'),
]
