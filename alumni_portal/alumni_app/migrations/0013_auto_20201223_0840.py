# Generated by Django 3.1.2 on 2020-12-23 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0012_placement_companies_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placement_companies_model',
            old_name='stipened',
            new_name='stipend',
        ),
    ]
