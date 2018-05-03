# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(default='Florida', max_length=7)),
                ('zip_code', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('estimate_id', models.AutoField(serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(default='Florida', max_length=7)),
                ('zip_code', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('customer', models.ForeignKey(blank=True, to='customers.CustomerProfile', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(serialize=False, primary_key=True)),
                ('customer', models.ForeignKey(to='customers.CustomerProfile')),
                ('estimate_id', models.OneToOneField(to='customers.Estimate')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('referral_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=100, blank=True)),
                ('customer', models.ForeignKey(to='customers.CustomerProfile')),
                ('estimate_id', models.OneToOneField(null=True, blank=True, to='customers.Estimate')),
            ],
        ),
    ]
