# Generated by Django 5.1.1 on 2024-10-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_remove_cart_products_watchupload_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='homepage.watchupload'),
        ),
    ]
