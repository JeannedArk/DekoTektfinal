# Generated by Django 4.0.5 on 2022-06-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_projectgallery_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectgallery',
            old_name='description1',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.AddField(
            model_name='projectgallery',
            name='construction_phase',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='projectgallery',
            name='country',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='projectgallery',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='projectgallery',
            name='design_phase',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='projectgallery',
            name='project_detail_name',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='projectgallery',
            name='video',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='projectgallery',
            name='year',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
