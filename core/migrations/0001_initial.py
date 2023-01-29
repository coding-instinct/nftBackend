# Generated by Django 3.2.8 on 2023-01-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenid', models.IntegerField(unique=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='nftimg/%Y/%m/%d/')),
            ],
        ),
    ]
