# Generated by Django 2.1 on 2019-03-23 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MonthlyAverage',
        ),
        migrations.DeleteModel(
            name='YearlyAverage',
        ),
    ]
