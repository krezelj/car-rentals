# Generated by Django 4.1.5 on 2023-01-23 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_rental_end_date_alter_rental_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rental',
            name='start_date',
            field=models.DateField(),
        ),
    ]
