# Generated by Django 3.1.2 on 2022-06-04 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distr_app', '0004_auto_20220603_2356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author_phtot',
            new_name='author_photo',
        ),
    ]
