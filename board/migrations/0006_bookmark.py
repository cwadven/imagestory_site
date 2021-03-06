# Generated by Django 3.0.7 on 2020-08-02 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200731_2028'),
        ('board', '0005_commentalertcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
