# Generated by Django 2.1.7 on 2019-05-30 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events_attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('id_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='attendance_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='registrant_info',
        ),
        migrations.AddField(
            model_name='event',
            name='about_event',
            field=models.CharField(default='', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendee_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events_attendance.Registration'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
    ]
