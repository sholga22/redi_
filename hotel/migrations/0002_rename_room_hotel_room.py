# Generated by Django 4.2.7 on 2023-11-26 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='hotel_Room',
        ),
    ]