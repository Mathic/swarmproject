from django.contrib.auth.models import User

from django.db import models

import plotly.plotly as py
import plotly.graph_objs as go

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class GraphData(models.Model):
    graph_year = models.IntegerField()
    average_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    average_precipitation = models.DecimalField(max_digits=5, decimal_places=2)
    source_text = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5, decimal_places=2)
    event = models.CharField(max_length=500, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.graph_year)

    @property
    def article_chart(self):
        data = [
            go.Bar(
                x=[self.graph_year], # years
                y=[self.average_temperature] # average_temperature
            )
        ]
        plot_url = py.plot(data, filename='basic-bar')

        return plot_url
