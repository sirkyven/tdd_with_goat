# Generated by Django 4.2.6 on 2023-10-27 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_list_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lists.list'),
        ),
    ]
