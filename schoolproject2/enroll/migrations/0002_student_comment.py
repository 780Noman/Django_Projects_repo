# Generated by Django 5.1 on 2024-08-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='not available', max_length=40),
        ),
    ]
