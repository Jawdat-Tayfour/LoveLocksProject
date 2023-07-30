# Generated by Django 4.2.3 on 2023-07-12 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("padlocks", "0004_alter_padlock_creator_alter_padlock_modifier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="padlock",
            name="creator",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="creator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="padlock",
            name="modifier",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="modifier",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]