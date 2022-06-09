# Generated by Django 4.0.2 on 2022-06-06 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='media/Project_details')),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]