# Generated by Django 3.0 on 2020-07-05 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200706_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_role',
            field=models.ImageField(choices=[('Customer', 'Customer'), ('Astrologer', 'Astrologer')], max_length=30, upload_to=''),
        ),
    ]