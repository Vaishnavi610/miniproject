# Generated by Django 3.1.7 on 2021-03-25 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_auto_20210325_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.user'),
        ),
    ]
