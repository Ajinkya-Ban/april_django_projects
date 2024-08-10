# Generated by Django 5.0.6 on 2024-08-05 11:36

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('prod_info', tinymce.models.HTMLField()),
                ('prod_img', models.ImageField(upload_to='media/prod_imgs/')),
            ],
        ),
    ]