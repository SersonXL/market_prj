# Generated by Django 3.2.25 on 2024-05-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
