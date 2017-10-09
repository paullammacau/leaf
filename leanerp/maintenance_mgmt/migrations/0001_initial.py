# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 14:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisement_mgmt', '0001_initial'),
        ('helpdesk', '0017_erppermisson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('code', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('discover_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, default='media/maintain_images/None/no-img.jpg', null=True, upload_to='media/maintain_images/')),
                ('validate_date', models.DateTimeField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisement_mgmt.Store')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.Ticket')),
            ],
            options={
                'permissions': (('maintenance_mgmt', '可以新增維修及查看當前維修'), ('allow_maintenance_validate', '可以審核維修申請單')),
            },
        ),
    ]
