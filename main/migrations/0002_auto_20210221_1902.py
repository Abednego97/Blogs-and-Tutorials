# Generated by Django 3.0.6 on 2021-02-21 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='Tut_Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 21, 19, 2, 14, 39423), verbose_name='date published'),
        ),
    ]
