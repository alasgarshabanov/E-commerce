# Generated by Django 3.1.4 on 2021-05-14 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.brand', verbose_name='Brand name'),
        ),
    ]