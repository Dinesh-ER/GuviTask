# Generated by Django 4.1 on 2022-08-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_users_age_users_contact_users_country_users_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]