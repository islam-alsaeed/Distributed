# Generated by Django 3.1.2 on 2022-06-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distr_app', '0003_auto_20220603_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
