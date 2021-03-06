# Generated by Django 3.1 on 2020-08-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20200829_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('registration_time', models.DateField(auto_now_add=True)),
                ('modify_time', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'user_database',
            },
        ),
    ]
