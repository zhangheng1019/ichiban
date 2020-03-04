# Generated by Django 2.1.7 on 2020-02-19 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POM', '0003_auto_20200216_1838'),
        ('Order', '0002_auto_20200204_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='po_detail',
            name='fac_ability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='factory_ability', to='POM.FactoryAbility', verbose_name='工厂产能信息'),
        ),
    ]