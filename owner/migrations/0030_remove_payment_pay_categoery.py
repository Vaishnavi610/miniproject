# Generated by Django 3.1.7 on 2021-05-15 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0029_auto_20210513_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='Pay_categoery',
        ),
    ]
