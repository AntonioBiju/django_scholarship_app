# Generated by Django 5.1.4 on 2025-01-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0009_scholarship_information_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="scholarship_information",
            name="link",
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
