# Generated by Django 3.0.5 on 2022-05-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]