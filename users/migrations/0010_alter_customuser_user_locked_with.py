# Generated by Django 4.2.3 on 2023-07-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0009_customuser_lock_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_locked_with",
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]
