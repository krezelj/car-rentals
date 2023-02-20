# Generated by Django 4.1.5 on 2023-01-23 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_transmission_vehicle_transmission_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='rental',
            name='dropoff_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dropoff_location', to='main.location'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='pickup_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup_location', to='main.location'),
        ),
    ]
