# Generated by Django 4.1.7 on 2023-03-10 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_db_mark', '0005_student_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='age',
            new_name='room',
        ),
    ]