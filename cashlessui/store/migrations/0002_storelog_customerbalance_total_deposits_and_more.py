# Generated by Django 5.1.3 on 2024-11-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loglevel', models.CharField(max_length=50)),
                ('module', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='customerbalance',
            name='total_deposits',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customerbalance',
            name='total_purchases',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customerbalance',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
