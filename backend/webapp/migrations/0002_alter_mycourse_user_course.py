# Generated by Django 5.0.1 on 2024-05-18 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycourse',
            name='user_course',
            field=models.CharField(max_length=50),
        ),
    ]
