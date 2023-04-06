# Generated by Django 4.1.7 on 2023-04-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('keterangan', models.CharField(max_length=250)),
                ('ukuran', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL'), ('All Size', 'All Size')], default='All Size', max_length=8)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
