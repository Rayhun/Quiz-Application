# Generated by Django 3.2.16 on 2022-11-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20221111_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]