# Generated by Django 2.1.7 on 2020-02-19 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_remove_po_detail_fty_ability'),
        ('POM', '0003_auto_20200216_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='factoryability',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ability_item', to='Order.Po_detail', verbose_name='工厂产能对应的item'),
        ),
    ]
