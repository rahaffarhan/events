from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Event


@receiver(post_save, sender=User)
def create_event(sender, instance, created, **kwargs):
    if created:
        Event.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_event(sender, instance, **kwargs):
        instance.event.save()


@receiver(post_save, sender=User)
def update_event(sender, instance, update_fields):
    instance.event.delete()

@receiver(post_delete, sender=User)
def delete_event(sender, instance, using):
    instance.event.delete()