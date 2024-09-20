# Generated by Django 5.0.4 on 2024-09-19 17:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eip', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestamp',
            name='timeVerified',
            field=models.DateTimeField(max_length=55),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='userVerifiedBy',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='verificationUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
