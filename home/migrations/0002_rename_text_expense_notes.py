# Generated by Django 4.2.7 on 2023-11-29 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='text',
            new_name='notes',
        ),
    ]