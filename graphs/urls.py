from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('month', views.monthly_graph, name='monthly_graph'),
    path('data_ottawa', views.data_ottawa, name='data_ottawa'),
    path('data_victoria', views.data_victoria, name='data_victoria'),
    path('data_month', views.data_m, name='data_m'),
    path('add', views.add_data, name='add_data'),
    path('test', views.test, name='test'),

    path('ajax/load-years', views.load_years, name='ajax_load_years'),
    path('ajax/save-data', views.save_data, name='ajax_save_data'),
    path('ajax/load-months', views.load_months, name='ajax_load_months'),
    path('api/chart/data', views.ClimateData.as_view(), name='api-chart-data'),
    path('api/chart/monthly-data', views.MonthlyData.as_view(), name='api-chart-monthly-data'),
]
