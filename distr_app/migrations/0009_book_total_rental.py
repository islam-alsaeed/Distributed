# Generated by Django 3.1.2 on 2022-06-06 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distr_app', '0008_auto_20220606_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
