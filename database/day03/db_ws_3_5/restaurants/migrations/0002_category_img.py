# Generated by Django 4.2.11 on 2024-10-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
