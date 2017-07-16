# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(help_text='Enter Poll option for Choosen Question', max_length=200, verbose_name='Poll Option')),
                ('votes', models.IntegerField(default=0, help_text='Enter Vote Count')),
                ('question', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='welcome.Question')),
            ],
        ),
    ]