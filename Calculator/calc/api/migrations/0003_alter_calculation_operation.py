# Generated by Django 5.1.2 on 2024-11-14 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_calculation_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calculation",
            name="operation",
            field=models.CharField(
                choices=[
                    ("add", "Addition"),
                    ("subtract", "Subtraction"),
                    ("multiply", "Multiplication"),
                    ("divide", "Division"),
                    ("module", "Modulus"),
                ],
                max_length=10,
            ),
        ),
    ]
