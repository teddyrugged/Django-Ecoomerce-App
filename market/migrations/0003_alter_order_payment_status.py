# Generated by Django 4.1 on 2022-08-09 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("market", "0002_address_zip"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_status",
            field=models.CharField(
                choices=[("P", "Pending"), ("C", "Complete"), ("F", "Failed")],
                default="P",
                max_length=1,
            ),
        ),
    ]
