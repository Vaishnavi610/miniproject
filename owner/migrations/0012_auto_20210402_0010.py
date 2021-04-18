# Generated by Django 3.1.6 on 2021-04-01 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0011_history_member_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount_paid', models.IntegerField(default=1, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('Member_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.user')),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('Beverages', 'Beverages'), ('Thali', 'Thali'), ('snaks', 'snacks')], max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='history',
        ),
    ]
