# Generated by Django 5.1.4 on 2025-01-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0011_scholarship_information_funding"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scholarship_information",
            name="funding",
            field=models.CharField(
                choices=[
                    ("Aided", "Aided"),
                    ("Self-Financed", "Self-Financed"),
                    ("All", "All"),
                ],
                default="All",
                max_length=15,
            ),
        ),
    ]
