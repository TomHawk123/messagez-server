# Generated by Django 4.0.5 on 2022-06-16 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0004_alter_reply_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default='default', max_length=1000),
        ),
    ]