# Generated by Django 4.2.7 on 2024-01-14 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_orderitem_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='created_by',
        ),
    ]
