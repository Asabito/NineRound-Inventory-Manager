# Generated by Django 4.1.7 on 2023-04-03 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0002_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='events',
            field=models.ManyToManyField(to='inventory_app.event'),
        ),
    ]
