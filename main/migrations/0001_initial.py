# Generated by Django 3.0.6 on 2020-08-12 16:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_category', models.CharField(max_length=200)),
                ('category_summary', models.CharField(max_length=200)),
                ('category_slug', models.CharField(default=1, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_series', models.CharField(max_length=200)),
                ('series_summary', models.CharField(max_length=200)),
                ('tutorial_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tut_Tittle', models.CharField(max_length=200)),
                ('Tut_Content', models.TextField()),
                ('Tut_Date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
                ('tutorial_slug', models.CharField(default=1, max_length=200)),
                ('tutorial_series', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Series', verbose_name='Series')),
            ],
        ),
    ]
