# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-24 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0016_alter_model_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ERPPermisson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('view_ERP_issues', '可以進入事項管理系統'),),
            },
        ),
    ]
