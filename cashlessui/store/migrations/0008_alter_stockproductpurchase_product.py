# Generated by Django 4.2.16 on 2024-11-16 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_stockproductpurchase_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockproductpurchase',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]