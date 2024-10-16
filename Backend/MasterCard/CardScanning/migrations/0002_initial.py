# Generated by Django 5.0.6 on 2024-10-16 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CardScanning', '0001_initial'),
        ('userManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='userManagement.customuser'),
        ),
        migrations.AddField(
            model_name='accesscontrol',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CardScanning.card'),
        ),
        migrations.AddField(
            model_name='cardscan',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CardScanning.card'),
        ),
        migrations.AddField(
            model_name='cardscan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='userManagement.customuser'),
        ),
        migrations.AddField(
            model_name='scanlog',
            name='scan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CardScanning.cardscan'),
        ),
    ]