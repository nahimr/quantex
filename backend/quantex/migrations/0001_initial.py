# Generated by Django 4.0.2 on 2022-03-07 14:32

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketData',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
                ('open', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('close', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('low', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('high', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('volume', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('dividends', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('stocks_splits', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('symbol', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('baseCurrency', models.CharField(max_length=3)),
                ('region', models.CharField(max_length=128)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quantex.marketdata')),
            ],
        ),
    ]