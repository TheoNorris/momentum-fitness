# Generated by Django 3.1 on 2020-08-18 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_merge_20200818_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='original_bag',
        ),
    ]