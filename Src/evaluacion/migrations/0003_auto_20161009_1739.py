# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0002_auto_20161006_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cumplimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=120, null=True, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='calificacion',
            name='cumplimiento',
        ),
    ]