# Generated by Django 2.2.8 on 2022-10-06 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoring', '0001_squashed_0007_auto_20220127_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='hour',
            field=models.IntegerField(choices=[(11, '11am'), (12, '12pm'), (13, '1pm'), (14, '2pm'), (15, '3pm'), (16, '4pm')]),
        ),
    ]
