# Generated by Django 4.0.5 on 2022-08-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_remove_school_profile_pic_school_hod_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='hod_name',
            field=models.CharField(default='Enter here', max_length=100),
        ),
    ]