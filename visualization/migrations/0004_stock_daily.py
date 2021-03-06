# Generated by Django 2.1.1 on 2018-10-11 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0003_auto_20181010_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_daily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10, verbose_name='Symbol')),
                ('open', models.FloatField(verbose_name='Open price')),
                ('high', models.FloatField(verbose_name='High price')),
                ('low', models.FloatField(verbose_name='Low price')),
                ('close', models.FloatField(verbose_name='Close price')),
                ('volume', models.FloatField(verbose_name='Volume')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Key in date')),
            ],
            options={
                'verbose_name': 'Stock daily',
                'ordering': ['symbol'],
            },
        ),
    ]
