# Generated by Django 3.2.4 on 2021-06-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_filebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='FileBook',
            field=models.FileField(blank=True, default='', null=True, upload_to=''),
        ),
    ]
