# Generated by Django 3.2.14 on 2022-10-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
