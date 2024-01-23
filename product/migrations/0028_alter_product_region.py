# Generated by Django 4.2.7 on 2024-01-17 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_alter_product_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='region',
            field=models.CharField(blank=True, choices=[('Auckland', 'Auckland'), ('Hamilton', 'Hamilton'), ('Tauranga', 'Tauranga'), ('Napier', 'Napier'), ('Palmerston North', 'Palmerston North'), ('Porirua', 'Porirua'), ('Upper Hutt', 'Upper Hutt'), ('Lower Hutt', 'Lower Hutt'), ('Wellington', 'Wellington'), ('Nelson', 'Nelson'), ('Christchurch', 'Christchurch'), ('Dunedin', 'Dunedin'), ('Invercargill', 'Invercargill'), ('North Island', 'North Island'), ('South Island', 'South Island'), ('Far North', 'Far North (Kaitaia)'), ('Kaipara', 'Kaipara (Dargaville)'), ('Whangarei', 'Whangarei (Whangarei)'), ('Hauraki', 'Hauraki (Paeroa)'), ('Matamata-Piako', 'Matamata-Piako (Matamata)'), ('Ōtorohanga', 'Ōtorohanga (Ōtorohanga)'), ('South Waikato', 'South Waikato (Tokoroa)'), ('Thames-Coromandel', 'Thames-Coromandel (Whitianga)'), ('Waikato', 'Waikato (Hamilton)'), ('Waipa', 'Waipa (Te Awamutu)'), ('Kawerau', 'Kawerau (Kawerau)'), ('Ōpōtiki', 'Ōpōtiki (Ōpōtiki)'), ('Western Bay of Plenty', 'Western Bay of Plenty (Tauranga)'), ('Whakatāne', 'Whakatāne (Whakatāne)'), ("Central Hawke's Bay", "Central Hawke's Bay (Waipawa)"), ('Hastings', 'Hastings (Hastings)'), ('Wairoa', 'Wairoa (Wairoa)'), ('New Plymouth', 'New Plymouth (New Plymouth)'), ('South Taranaki', 'South Taranaki (Hawera)'), ('Horowhenua', 'Horowhenua (Levin)'), ('Manawatū', 'Manawatū (Palmerston North)'), ('Ruapehu', 'Ruapehu (Ohakune)'), ('Whanganui', 'Whanganui (Whanganui)'), ('Carterton', 'Carterton (Carterton)'), ('Kāpiti Coast', 'Kāpiti Coast (Paraparaumu)'), ('Masterton', 'Masterton (Masterton)'), ('South Wairarapa', 'South Wairarapa (Martinborough)'), ('Rangitikei', 'Rangitikei (Marton)'), ('Rotorua Lakes', 'Rotorua Lakes (Rotorua)'), ('Stratford', 'Stratford (Stratford)'), ('Tararua', 'Tararua (Dannevirke)'), ('Taupō', 'Taupō (Taupō)'), ('Waitomo', 'Waitomo (Te Kuiti)'), ('Gisborne', 'Gisborne (Gisborne)'), ('Buller', 'Buller (Westport)'), ('Grey', 'Grey (Greymouth)'), ('Westland', 'Westland (Hokitika)'), ('Ashburton', 'Ashburton (Ashburton)'), ('Hurunui', 'Hurunui (Amberley)'), ('Kaikōura', 'Kaikōura (Kaikōura)'), ('Mackenzie', 'Mackenzie (Fairlie)'), ('Selwyn', 'Selwyn (Rolleston)'), ('Timaru', 'Timaru (Timaru)'), ('Waimakariri', 'Waimakariri (Rangiora)'), ('Waimate', 'Waimate (Waimate)'), ('Central Otago', 'Central Otago (Alexandra)'), ('Clutha', 'Clutha (Balclutha)'), ('Queenstown-Lakes', 'Queenstown-Lakes (Queenstown)'), ('Gore', 'Gore (Gore)'), ('Southland', 'Southland (Invercargill)'), ('Waitaki', 'Waitaki (Oamaru)'), ('Marlborough', 'Marlborough (Blenheim)'), ('Tasman', 'Tasman (Richmond)')], max_length=50, null=True),
        ),
    ]
