# Generated by Django 4.1.4 on 2022-12-14 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecondHandProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_hand_product_name', models.CharField(max_length=40)),
                ('second_hand_product_image', models.URLField()),
                ('second_hand_product_price', models.FloatField()),
                ('second_hand_product_description', models.TextField(blank=True, max_length=1200)),
                ('second_hand_uploaded_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
