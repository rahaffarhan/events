# Generated by Django 2.1.7 on 2019-06-01 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_attendance', '0003_auto_20190531_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
