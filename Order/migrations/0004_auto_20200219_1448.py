# Generated by Django 2.1.7 on 2020-02-19 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_po_detail_fac_ability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='po_detail',
            name='fac_ability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ability', to='POM.FactoryAbility', verbose_name='工厂产能信息'),
        ),
    ]