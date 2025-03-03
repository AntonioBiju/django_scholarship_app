# Generated by Django 5.1.4 on 2025-01-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalinformation",
            name="caste",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Scheduled Caste", "Scheduled Caste"),
                    ("Scheduled Tribe", "Scheduled Tribe"),
                    ("Minorities", "Minorities"),
                    ("OBC", "OBC"),
                    ("Nomadic Tribes", "Nomadic Tribes"),
                    ("SC", "SC"),
                    ("SEBC", "SEBC"),
                    ("MBC", "MBC"),
                    ("Other Backward Class", "Other Backward Class"),
                    ("Vimukta Jati", "Vimukta Jati"),
                    ("EWS", "EWS"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="personalinformation",
            name="diploma_field",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Polytechnic", "Polytechnic"),
                    ("Vocational", "Vocational"),
                    ("ITI", "ITI"),
                    ("Other", "Other"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="personalinformation",
            name="pg_degree",
            field=models.CharField(
                blank=True,
                choices=[
                    ("M.Tech", "M.Tech"),
                    ("M.Sc", "M.Sc"),
                    ("M.Com", "M.Com"),
                    ("M.A", "M.A"),
                    ("Other", "Other"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="personalinformation",
            name="ug_degree",
            field=models.CharField(
                blank=True,
                choices=[
                    ("B.Tech", "B.Tech"),
                    ("B.Sc", "B.Sc"),
                    ("B.Com", "B.Com"),
                    ("B.A", "B.A"),
                    ("Other", "Other"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
