# Generated by Django 5.0.7 on 2024-09-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_student_residence'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
