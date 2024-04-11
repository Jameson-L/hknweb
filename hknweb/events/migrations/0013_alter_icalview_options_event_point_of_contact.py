# Generated by Django 4.2.5 on 2024-03-14 22:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0012_icalview"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="icalview",
            options={"verbose_name": "iCal view"},
        ),
        migrations.AddField(
            model_name="event",
            name="point_of_contact",
            field=models.CharField(default="N/A", max_length=255),
        ),
    ]