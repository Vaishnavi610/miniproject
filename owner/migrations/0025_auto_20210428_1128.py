# Generated by Django 3.1.7 on 2021-04-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0024_auto_20210427_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notcome',
            name='Ending_date',
        ),
        migrations.RemoveField(
            model_name='notcome',
            name='Starting_date',
        ),
        migrations.AddField(
            model_name='notcome',
            name='Date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]