# Generated by Django 2.1 on 2022-06-12 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20220611_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('thumb_id', models.CharField(max_length=32)),
                ('ec_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]
