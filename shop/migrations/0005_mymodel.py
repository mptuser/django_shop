# Generated by Django 3.1.1 on 2021-03-13 11:23

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210313_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/img'), upload_to='')),
            ],
        ),
    ]
