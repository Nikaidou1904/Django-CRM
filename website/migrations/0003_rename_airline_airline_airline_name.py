# Generated by Django 5.1.3 on 2024-11-21 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_airline_backpack'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airline',
            old_name='airline',
            new_name='airline_name',
        ),
    ]