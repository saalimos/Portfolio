# Generated by Django 5.2 on 2025-04-29 05:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0007_profiledb_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechStackDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='tech_icons/')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.profiledb')),
            ],
        ),
        migrations.DeleteModel(
            name='SkillDB',
        ),
    ]
