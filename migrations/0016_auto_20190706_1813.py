# Generated by Django 2.2.2 on 2019-07-06 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events_attendance', '0015_auto_20190705_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='event_name',
        ),
    ]
