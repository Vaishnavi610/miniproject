# Generated by Django 3.1.7 on 2021-04-28 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0028_auto_20210428_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notcome',
            old_name='From',
            new_name='From_date',
        ),
        migrations.RenameField(
            model_name='notcome',
            old_name='To',
            new_name='To_date',
        ),
    ]