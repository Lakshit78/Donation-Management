# Generated by Django 5.0.2 on 2024-07-28 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=100)),
                ('donator', models.CharField(max_length=100)),
            ],
        ),
    ]