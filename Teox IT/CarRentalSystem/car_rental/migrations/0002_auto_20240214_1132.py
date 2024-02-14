# Generated by Django 3.2.19 on 2024-02-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbooking',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='carbooking',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
