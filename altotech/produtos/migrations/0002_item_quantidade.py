# Generated by Django 4.2.4 on 2023-08-24 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantidade',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]