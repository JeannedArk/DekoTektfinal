# Generated by Django 4.0.5 on 2022-06-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_projectgallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectgallery',
            options={'verbose_name': 'projectgallery', 'verbose_name_plural': 'project gallery'},
        ),
        migrations.AddField(
            model_name='projectgallery',
            name='description1',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
