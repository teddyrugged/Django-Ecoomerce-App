# Generated by Django 2.2.6 on 2022-08-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default=None, max_length=6),
        ),
    ]