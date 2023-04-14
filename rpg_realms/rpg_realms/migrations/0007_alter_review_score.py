# Generated by Django 4.2 on 2023-04-13 20:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rpg_realms", "0006_alter_review_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="score",
            field=models.IntegerField(
                default=5,
                validators=[
                    django.core.validators.MaxValueValidator(11),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
    ]
