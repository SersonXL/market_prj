# Generated by Django 3.2.25 on 2024-05-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]