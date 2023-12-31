# Generated by Django 4.2 on 2023-06-29 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pnwanderer', '0005_delete_detailedpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='updated_at',
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='featured_image/%Y/%m/%d/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pnwanderer.blogpost')),
            ],
        ),
    ]
