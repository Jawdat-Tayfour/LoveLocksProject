# Generated by Django 4.2.3 on 2023-07-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("padlocks", "0005_alter_padlock_creator_alter_padlock_modifier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="padlock",
            name="active_state",
            field=models.BooleanField(default=False),
        ),
    ]
