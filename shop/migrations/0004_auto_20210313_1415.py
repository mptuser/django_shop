# Generated by Django 3.1.1 on 2021-03-13 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210313_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Изображение продукта'),
        ),
    ]
