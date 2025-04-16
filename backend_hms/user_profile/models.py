from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    class Meta:
        db_table = 'user_profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    blood_types = (
        (1, '0-'),
        (2, '0+'),
        (3, 'A-'),
        (4, 'A+'),
        (5, 'B-'),
        (6, 'B+'),
        (7, 'AB+'),
        (8, 'AB-'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True)
    address = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    blood = models.IntegerField(choices=blood_types, null=True, blank=True)
    allergies = models.TextField(blank=True, null=True)
    chronic_disease = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Профиль {self.user.first_name} {self.user.last_name}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

