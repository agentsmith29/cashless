# Generated by Django 5.1.3 on 2024-12-01 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_storeproduct_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerpurchase',
            name='expenses',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='customerpurchase',
            name='revenue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining_quantity', models.PositiveIntegerField(default=0)),
                ('restock', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='store.productrestock')),
            ],
        ),
    ]
