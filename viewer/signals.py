from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import OperatorProfile
from .models import OperatorPoints

@receiver(post_save, sender=User)
def create_operator_profile(sender, instance, created, **kwargs):
    if created:
        OperatorProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_operator_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

@receiver(post_save, sender=User)
def create_operator_points(sender, instance, created, **kwargs):
    if created:
        OperatorPoints.objects.create(user=instance)