# Generated by Django 4.2.7 on 2023-12-31 19:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0008_order_orderitem"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="merchant_id",
            new_name="payment_intent",
        ),
    ]
