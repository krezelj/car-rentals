# Generated by Django 4.1.5 on 2023-01-23 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_location_alter_rental_dropoff_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='rental',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
