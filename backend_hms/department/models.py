from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):

    class Meta:
        db_table = 'departments'
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

    title = models.CharField(max_length=40, verbose_name="Отделение")
    doctors = models.ManyToManyField(User, related_name='departments', verbose_name="Врачи")
    sub_title = models.TextField(max_length=200, verbose_name="Описание")
    link = models.CharField(max_length=40, verbose_name="Иконка")


    def __str__(self):
        return self.title

