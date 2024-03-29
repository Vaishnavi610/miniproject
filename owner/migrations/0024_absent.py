# Generated by Django 3.1.7 on 2021-05-11 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0023_auto_20210510_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('Time', models.CharField(choices=[('Day', 'Day'), ('Night', 'Night'), ('Both', 'Both')], max_length=50, null=True)),
                ('Day', models.CharField(choices=[('Today', 'Today'), ('More', 'More')], max_length=50, null=True)),
                ('From_date', models.DateField(null=True)),
                ('To_date', models.DateField(null=True)),
                ('Member_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.user')),
            ],
        ),
    ]
