# Generated by Django 4.2.8 on 2023-12-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0003_url_key_alter_url_shorted_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='access_counter',
            field=models.IntegerField(default=0),
        ),
    ]