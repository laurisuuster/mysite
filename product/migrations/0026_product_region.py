# Generated by Django 4.2.7 on 2024-01-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_remove_product_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='region',
            field=models.CharField(blank=True, choices=[('North Island', 'North Island'), ('South Island', 'South Island')], max_length=50, null=True),
        ),
    ]
