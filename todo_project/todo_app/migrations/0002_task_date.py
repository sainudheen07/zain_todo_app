# Generated by Django 3.1.7 on 2021-04-28 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 28)),
        ),
    ]
