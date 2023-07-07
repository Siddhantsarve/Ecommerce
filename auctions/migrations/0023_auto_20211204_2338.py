# Generated by Django 3.2.8 on 2021-12-04 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20211204_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='item',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
    ]
