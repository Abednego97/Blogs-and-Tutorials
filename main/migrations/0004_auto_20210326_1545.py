# Generated by Django 3.0.6 on 2021-03-26 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210303_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='Tut_Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 15, 45, 1, 743364), verbose_name='date published'),
        ),
    ]
