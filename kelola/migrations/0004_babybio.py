# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 06:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kelola', '0003_knowledge'),
    ]

    operations = [
        migrations.CreateModel(
            name='BabyBio',
            fields=[
                ('id_baby', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('baby_name', models.CharField(max_length=100)),
                ('date_birth', models.DateField(blank=True, null=True)),
                ('address', models.TextField()),
                ('mother_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('weight_birth', models.IntegerField(max_length=2)),
                ('height_birth', models.IntegerField(max_length=2)),
                ('headcircumference_birth', models.IntegerField(max_length=3)),
            ],
        ),
    ]