# Generated by Django 3.1.2 on 2022-06-03 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distr_app', '0002_auto_20220603_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=5, null=True),
        ),
    ]
