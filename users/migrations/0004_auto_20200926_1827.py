# Generated by Django 3.0.6 on 2020-09-26 18:27

from django.db import migrations, models
import users.validation


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200925_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='birth_date'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=10, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='student_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
