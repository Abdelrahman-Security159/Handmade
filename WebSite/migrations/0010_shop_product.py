# Generated by Django 4.2.7 on 2025-03-28 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0009_product_alter_shop_buyer_alter_shop_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WebSite.product'),
        ),
    ]
