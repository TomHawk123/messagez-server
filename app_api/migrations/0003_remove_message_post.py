# Generated by Django 4.0.5 on 2022-06-13 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0002_zasuser_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='post',
        ),
    ]
