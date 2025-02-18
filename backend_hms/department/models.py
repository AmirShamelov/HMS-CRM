from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):

    class Meta:
        db_table = 'departments'

    title = models.CharField(max_length=40)
    doctors = models.ManyToManyField(User, related_name='departments')
    sub_title = models.CharField(max_length=200)
    link = models.CharField(max_length=40)


    def __str__(self):
        return self.title