# Generated by Django 2.2.2 on 2019-07-01 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_attendance', '0010_auto_20190630_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
