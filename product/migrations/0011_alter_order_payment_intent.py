# Generated by Django 4.2.7 on 2023-12-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0010_alter_order_payment_intent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_intent",
            field=models.CharField(max_length=255),
        ),
    ]
