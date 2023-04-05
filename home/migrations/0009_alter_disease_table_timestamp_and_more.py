# Generated by Django 4.1.7 on 2023-04-04 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_alter_disease_table_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disease_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 4, 10, 57, 0, 943287, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="key_value_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 4, 10, 57, 0, 944381, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="testimonial_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 4, 10, 57, 0, 943790, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="video_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 4, 10, 57, 0, 944060, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]