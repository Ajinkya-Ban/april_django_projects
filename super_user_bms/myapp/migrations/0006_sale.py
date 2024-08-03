# Generated by Django 5.0.6 on 2024-07-31 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_product_options_alter_unit_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField()),
                ('price', models.FloatField()),
                ('total_amt', models.FloatField()),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=50)),
                ('cutomer_mob', models.CharField(max_length=10)),
                ('customer_add', models.CharField(max_length=150)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
            options={
                'verbose_name_plural': 'Sale',
            },
        ),
    ]