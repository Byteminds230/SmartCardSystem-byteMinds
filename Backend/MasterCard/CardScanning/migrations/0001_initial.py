# Generated by Django 5.0.6 on 2024-10-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_location', models.CharField(max_length=255)),
                ('access_time', models.TimeField()),
                ('is_granted', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(blank=True, null=True, unique=True)),
                ('card_type', models.CharField(choices=[('NFC', 'NFC'), ('RFID', 'RFID')], max_length=50)),
                ('issued_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('daily_scan_count', models.IntegerField(default=0)),
                ('last_scan_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardScan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('scan_date', models.DateTimeField(auto_now_add=True)),
                ('scan_result', models.TextField()),
                ('status', models.CharField(choices=[('Success', 'Success'), ('Failed', 'Failed')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScanDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100)),
                ('device_type', models.CharField(choices=[('NFC Reader', 'NFC Reader'), ('RFID Reader', 'RFID Reader')], max_length=50)),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ScanLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('log_type', models.CharField(choices=[('INFO', 'INFO'), ('WARNING', 'WARNING'), ('ERROR', 'ERROR')], max_length=50)),
            ],
        ),
    ]
