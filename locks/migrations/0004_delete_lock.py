# Generated by Django 4.2.3 on 2023-07-17 21:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("locks", "0003_delete_lockpost"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Lock",
        ),
    ]