from django.urls import path

from . import views

urlpatterns = [
    path('api/chart/data', views.ClimateData.as_view(), name='api-chart-data'),
    path('', views.index, name='index'),
    path('add', views.add_data, name='add_data'),

    path('ajax/load-years', views.load_years, name='ajax_load_years'),
    path('ajax/save-data', views.save_data, name='ajax_save_data'),
]
