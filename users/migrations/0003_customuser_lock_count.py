# Generated by Django 4.2.3 on 2023-07-11 12:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_customuser_lock_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="lock_count",
            field=models.PositiveIntegerField(
                default=7,
                validators=[
                    django.core.validators.MaxValueValidator(8),
                    django.core.validators.MinValueValidator(0),
                ],
            ),
        ),
    ]
