# Generated by Django 4.0.4 on 2022-06-16 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_project_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ImageField(upload_to='Projects'),
        ),
        migrations.AlterField(
            model_name='projectgallery',
            name='image',
            field=models.ImageField(max_length=255, upload_to='Project_details'),
        ),
    ]
