# Generated by Django 4.0.2 on 2022-03-20 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quantex', '0002_instrument_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrument',
            name='baseCurrency',
        ),
    ]