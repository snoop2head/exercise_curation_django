# Generated by Django 3.0.3 on 2020-02-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_auto_20200225_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]