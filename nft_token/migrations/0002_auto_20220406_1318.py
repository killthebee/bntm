# Generated by Django 3.1 on 2022-04-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft_token', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='unique_hash',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]