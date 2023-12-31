# Generated by Django 4.2.3 on 2023-07-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PadLock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("motto_field", models.CharField(max_length=200)),
                ("story_field", models.TextField(blank=True, max_length=20000)),
                ("active_state", models.BooleanField(default=True)),
            ],
        ),
    ]
