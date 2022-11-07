# Generated by Django 3.2.16 on 2022-11-07 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='is_delete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='order',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='is_delete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='is_delete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
