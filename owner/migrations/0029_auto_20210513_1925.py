# Generated by Django 3.1.6 on 2021-05-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0028_auto_20210513_1033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-Date_added']},
        ),
    ]
