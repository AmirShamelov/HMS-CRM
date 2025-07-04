# Generated by Django 4.2 on 2025-06-24 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=12, verbose_name='Номер телефона')),
                ('address', models.TextField(blank=True, verbose_name='Адрес')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('blood', models.IntegerField(blank=True, choices=[(1, '0-'), (2, '0+'), (3, 'A-'), (4, 'A+'), (5, 'B-'), (6, 'B+'), (7, 'AB+'), (8, 'AB-')], null=True, verbose_name='Группа крови')),
                ('allergies', models.TextField(blank=True, null=True, verbose_name='Аллергия')),
                ('chronic_disease', models.TextField(blank=True, null=True, verbose_name='Хроническое заболевание')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'db_table': 'user_profile',
            },
        ),
    ]
