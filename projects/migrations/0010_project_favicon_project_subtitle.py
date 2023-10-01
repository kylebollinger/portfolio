# Generated by Django 4.2.5 on 2023-09-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_gallery_options_alter_galleryitem_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='favicon',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='subtitle',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]