from django.urls import path

from . import views

urlpatterns = [
    # running scripts
    path('test', views.test, name='test'),

    # page loaders
    path('', views.index, name='index'),
    path('graphs', views.graphs, name='graphs'),
    path('data_ottawa', views.data_ottawa, name='data_ottawa'),
    path('data_victoria', views.data_victoria, name='data_victoria'),
    path('data_month', views.data_m, name='data_month'),
    path('add', views.add_data, name='add_data'),

    # ajax requests
    path('ajax/load-months', views.load_months, name='ajax_load_months'),
    path('ajax/load-years', views.load_years, name='ajax_load_years'),
    path('ajax/save-data', views.save_data, name='ajax_save_data'),

    # graph APIs
    path('api/chart/year_avg_temp', views.YearAvgTemp.as_view(), name='year_avg_temp'),
    path('api/chart/year_avg_prec', views.YearAvgPrec.as_view(), name='year_avg_prec'),
    path('api/chart/month_avg_temp', views.MonthAvgTemp.as_view(), name='month_avg_temp'),
    path('api/chart/month_avg_prec', views.MonthAvgPrec.as_view(), name='month_avg_prec'),
]
