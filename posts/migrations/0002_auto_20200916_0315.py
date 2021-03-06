# Generated by Django 3.0.6 on 2020-09-16 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.AddField(
            model_name='post',
            name='mediafile',
            field=models.FileField(default='', upload_to='mediafiles/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
