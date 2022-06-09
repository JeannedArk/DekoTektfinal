# Generated by Django 4.0.5 on 2022-06-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_projectgallery_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectgallery',
            name='city',
        ),
        migrations.RemoveField(
            model_name='projectgallery',
            name='construction_phase',
        ),
        migrations.RemoveField(
            model_name='projectgallery',
            name='country',
        ),
        migrations.RemoveField(
            model_name='projectgallery',
            name='description',
        ),
        migrations.RemoveField(
            model_name='projectgallery',
            name='design_phase',
        ),
        migrations.RemoveField(
            model_name='projectgallery',
            name='project_detail_name',
        ),
        migrations.RemoveField(
            model_name='projectgallery',
            name='video',
        ),
        migrations.RemoveField(
            model_name='projectgallery',
            name='year',
        ),
        migrations.AddField(
            model_name='project',
            name='city',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='construction_phase',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='country',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='project',
            name='design_phase',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='project_detail_name',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='video',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]