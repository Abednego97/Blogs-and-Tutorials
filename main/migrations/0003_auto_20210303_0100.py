# Generated by Django 3.0.6 on 2021-03-02 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210221_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='Tut_Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 1, 0, 9, 109528), verbose_name='date published'),
        ),
    ]
