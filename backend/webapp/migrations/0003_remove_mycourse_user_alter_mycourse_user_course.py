# Generated by Django 5.0.1 on 2024-05-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_mycourse_user_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycourse',
            name='user',
        ),
        migrations.AlterField(
            model_name='mycourse',
            name='user_course',
            field=models.CharField(default='Python', max_length=50),
        ),
    ]
