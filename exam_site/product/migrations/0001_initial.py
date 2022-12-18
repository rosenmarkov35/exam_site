# Generated by Django 4.1.4 on 2022-12-16 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40)),
                ('product_image', models.URLField()),
                ('product_price', models.FloatField()),
                ('product_description', models.TextField(blank=True, max_length=1200)),
                ('product_details', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]