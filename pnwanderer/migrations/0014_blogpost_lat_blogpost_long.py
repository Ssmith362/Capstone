# Generated by Django 4.2 on 2023-07-11 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnwanderer', '0013_blogpost_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='lat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='long',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]