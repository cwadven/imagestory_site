# Generated by Django 3.0.7 on 2020-06-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='secure',
            field=models.CharField(choices=[('public', '공개'), ('private', '비공개')], default=1, max_length=7),
            preserve_default=False,
        ),
    ]
