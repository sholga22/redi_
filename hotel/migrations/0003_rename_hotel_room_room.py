# Generated by Django 4.2.7 on 2023-11-27 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_rename_room_hotel_room'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='hotel_Room',
            new_name='Room',
        ),
    ]