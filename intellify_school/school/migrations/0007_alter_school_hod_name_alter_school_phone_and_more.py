# Generated by Django 4.0.5 on 2022-08-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_school_hod_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='hod_name',
            field=models.CharField(default='Enter HOD Name here', max_length=100),
        ),
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=models.CharField(default='Enter Phone no. here', max_length=100),
        ),
        migrations.AlterField(
            model_name='school',
            name='students_no',
            field=models.CharField(default='Enter no. of students here', max_length=100),
        ),
    ]
