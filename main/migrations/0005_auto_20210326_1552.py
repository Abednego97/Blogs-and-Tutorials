# Generated by Django 3.0.6 on 2021-03-26 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210326_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='Tut_Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 15, 52, 28, 165065), verbose_name='date published'),
        ),
    ]