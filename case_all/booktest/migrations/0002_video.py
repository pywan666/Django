# Generated by Django 3.1 on 2020-08-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('video', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=200)),
            ],
        ),
    ]