# Generated by Django 3.1.3 on 2020-11-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeblog', '0004_auto_20201124_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(),
        ),
    ]
