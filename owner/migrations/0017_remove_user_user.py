# Generated by Django 3.1.6 on 2021-04-12 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0016_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
    ]
