# Generated by Django 4.1 on 2022-08-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=12)),
                ('age', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=30)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
