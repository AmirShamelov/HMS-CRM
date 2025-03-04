from django.db import models
from django.contrib.auth.models import User
from department.models import Department

class Doctor(models.Model):
    doctor = models.ForeignKey(User, related_name='doctors', verbose_name='Врач', on_delete=models.CASCADE)
    education = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    department = models.ForeignKey(Department, related_name='staff', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='doctors_images', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return f'Врач {self.position} {self.doctor.first_name} {self.doctor.last_name}'

    class Meta:
        db_table = 'doctors'
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

