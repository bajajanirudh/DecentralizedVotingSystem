# Generated by Django 2.1 on 2018-10-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20181011_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
