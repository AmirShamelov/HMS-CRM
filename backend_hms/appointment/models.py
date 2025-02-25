from django.contrib.auth.models import User
from django.db import models

from department.models import Department

class Appointment(models.Model):
    TIME_CHOICES = (
        (1, '9:00-9:30'),
        (2, '9:30-10:00'),
        (3, '10:00-10:30'),
        (4, '10:30-11:00'),
        (5, '11:00-11:30'),
        (6, '11:30-12:00'),
        (7, '12:00-12:30'),
        (8, '12:30-13:00'),
        (9, '14:30-15:00'),
        (10, '15:00-15:30'),
        (11, '15:30-16:00'),
        (12, '16:00-16:30'),
        (13, '16:30-17:00'),
        (14, '17:00-17:30'),
        (15, '17:30-18:00'),
    )

    patient_name = models.CharField(max_length=100, verbose_name='Имя пациента')
    patient_iin = models.CharField(max_length=12, verbose_name='ИИН пациента')
    department = models.ForeignKey(Department, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='appointments', verbose_name='Врач', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата приема')
    time = models.IntegerField(choices=TIME_CHOICES, verbose_name='Время приема')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    created_by = models.ForeignKey(User, related_name='patients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Запись {self.created_by.first_name} на {self.date} в {self.get_time_display()} к {self.doctor.first_name} {self.doctor.last_name}'

    class Meta:
        db_table = 'appointments'
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'