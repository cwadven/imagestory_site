# Generated by Django 3.0.7 on 2021-01-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_auto_20200816_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to='board_picture_thumbnail/'),
        ),
    ]
