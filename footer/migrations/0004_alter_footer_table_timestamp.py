# Generated by Django 4.1.7 on 2023-04-04 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("footer", "0003_alter_footer_table_timestamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footer_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 4, 17, 34, 37, 232955)
            ),
        ),
    ]
