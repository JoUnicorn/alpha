# Generated by Django 2.1.1 on 2018-10-10 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0002_auto_20181010_2110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['symbol'], 'verbose_name': 'Stock data'},
        ),
    ]
