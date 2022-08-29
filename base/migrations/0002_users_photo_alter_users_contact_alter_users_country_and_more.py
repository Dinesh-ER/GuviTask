# Generated by Django 4.1 on 2022-08-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='users',
            name='contact',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='users',
            name='country',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='users',
            name='dob',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]