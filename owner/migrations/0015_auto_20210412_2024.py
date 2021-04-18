# Generated by Django 3.1.6 on 2021-04-12 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('owner', '0014_auto_20210411_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Member_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.user'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Member_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
