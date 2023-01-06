# Generated by Django 4.1.4 on 2022-12-27 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='Address',
        ),
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.date(2022, 12, 27)),
        ),
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(default='Description'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='email', max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='firstName',
            field=models.CharField(default='anonymous', max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='lastName',
            field=models.CharField(default='fighter', max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='+92', max_length=12),
        ),
    ]