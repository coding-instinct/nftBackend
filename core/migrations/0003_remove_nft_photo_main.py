# Generated by Django 3.2.8 on 2023-01-29 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_nft_urlpic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nft',
            name='photo_main',
        ),
    ]
