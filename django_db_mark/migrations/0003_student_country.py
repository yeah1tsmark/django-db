# Generated by Django 4.1.7 on 2023-03-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_db_mark', '0002_rename_students_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.CharField(default='kenya', max_length=50),
        ),
    ]