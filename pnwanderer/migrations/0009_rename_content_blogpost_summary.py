# Generated by Django 4.2 on 2023-06-29 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pnwanderer', '0008_alter_postimage_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='content',
            new_name='summary',
        ),
    ]