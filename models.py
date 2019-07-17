from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def create_profile(sender,**kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)


class Event(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               related_name='author')
    event_name = models.CharField(max_length=100)
    pic = models.ImageField(default='default-event.jpg', upload_to='event pictures')
    location = models.CharField(max_length=150, default='')
    location_url = models.URLField(max_length=255, blank=True, default="")
    content = models.TextField(default="about event")
    starts = models.DateTimeField(blank=True, null=True)
    ends = models.DateTimeField(blank=True, null=True)
    registration_starts = models.DateTimeField(blank=True, null=True)
    registration_ends = models.DateTimeField(blank=True, null=True)
    attendees_limits = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    event_date = models.DateField()
    organizers = models.CharField(max_length=100, default='')
    attendees = models.ManyToManyField(User, blank=True,
                                       related_name='attendees')

    class Meta:
        verbose_name = 'event'
        ordering = ['-event_date']

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.event_name

    def snippet(self):
        return self.content[:30]

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

    def save_pic(self):
        super().save()

        image = Image.open(self.pic.path)

        if image.height > 200 or image.width > 300:
            output_size = (200, 200)
            image.thumbnail(output_size)
            image.save(self.pic.path)
        else:
            output_size = (200, 200)
            image.thumbnail(output_size)
            image.save(self.pic.path)


class Club(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=500)
    leader = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='leader')
    email = models.EmailField()
    members = models.ManyToManyField(User,

                                     blank=True,
                                     null=True,
                                     related_name='members')

    events = models.ManyToManyField(Event)

    def __unicode__(self):
        return self.name


class EventRegistration(models.Model):
    registrant = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True,
                                   related_name='registrant')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
    time_submitted = models.DateTimeField(auto_now=True)
    is_confirmed = models.BooleanField(default=None)
    is_deleted = models.BooleanField(default=False)

    def check_register(self):
        if self.is_deleted == True:
            return "404"
        else:
            return self.is_confirmed

    def __unicode__(self):
        return u"{} for {}".format(self.user.username, self.event.event_name)


class EventAttendance(models.Model):
    attendee = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)
    event_registration = models.ForeignKey(EventRegistration,
                                           on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=None)

    def check_attendance(self):
        if self.is_deleted == True:
            return "deleted"
        else:
            return self.is_confirmed

    def __unicode__(self):
        return u"{} for {}".format(self.event_registration.user.username, self.event_registration.event.event_name)












