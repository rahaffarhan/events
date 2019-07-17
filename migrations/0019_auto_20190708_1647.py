# Generated by Django 2.2.2 on 2019-07-08 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events_attendance', '0018_auto_20190707_1531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-event_date'], 'verbose_name': 'event'},
        ),
        migrations.AddField(
            model_name='event',
            name='attendee_limits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='ends',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='event',
            name='location_url',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='registration_ends',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='registration_starts',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='starts',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_registered', models.DateTimeField()),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events_attendance.Event')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='attendee')),
            ],
            options={
                'ordering': ['time_registered'],
                'unique_together': {('event', 'user')},
            },
        ),
    ]
