# Generated by Django 5.1.3 on 2024-12-03 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="marks",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="student",
            name="standard",
            field=models.IntegerField(),
        ),
    ]