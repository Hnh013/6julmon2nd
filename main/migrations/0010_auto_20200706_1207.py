# Generated by Django 3.0 on 2020-07-06 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_auto_20200706_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astro_profile',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]