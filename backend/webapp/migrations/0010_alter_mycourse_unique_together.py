# Generated by Django 5.0.1 on 2024-06-09 06:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_mycourse_user_course_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mycourse',
            unique_together={('user', 'user_title')},
        ),
    ]