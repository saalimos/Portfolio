# Generated by Django 5.2 on 2025-04-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0015_experiencedb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencedb',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
