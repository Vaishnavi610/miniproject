# Generated by Django 3.1.7 on 2021-04-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0031_auto_20210428_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absent',
            name='From_date',
            field=models.DateField(null=True),
        ),
    ]