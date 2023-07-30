# Generated by Django 4.2.3 on 2023-07-16 19:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("padlocks", "0010_alter_padlock_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="padlock",
            name="story_field",
            field=models.TextField(
                blank=True,
                max_length=20000,
                validators=[django.core.validators.MinLengthValidator(4000)],
            ),
        ),
    ]