# Generated by Django 4.0.5 on 2022-06-16 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0003_remove_message_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='app_api.post'),
        ),
    ]
