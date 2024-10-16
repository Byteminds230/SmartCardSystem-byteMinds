from django.db import models
from userManagement.models import CustomUser
from django.core.exceptions import ValidationError
from django.utils import timezone
import random


class Card(models.Model):
    card_number = models.IntegerField(unique=True, null=True, blank=True)
    card_type = models.CharField(max_length=50, choices=[('NFC', 'NFC'), ('RFID', 'RFID')])
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True , related_name='user')
    issued_date = models.DateField()
    expiry_date = models.DateField()
    is_active = models.BooleanField(default=True)
    daily_scan_count = models.IntegerField(default=0)  # Tracks the number of scans per day
    last_scan_date = models.DateField(null=True, blank=True)  # Date of the last scan

    def __str__(self):
        return f'Card Number: {self.card_number} ({self.card_type})'

    def save(self, *args, **kwargs):
        # Check if the card is expired before saving
        self.check_expiry()

        # Generate a random card_number if not already set
        if self.card_number is None:
            self.card_number = random.randint(0, 16)

        # Ensure the card number is unique
        while Card.objects.filter(card_number=self.card_number).exists():
            self.card_number = random.randint(0, 16)

        super().save(*args, **kwargs)

    def check_expiry(self):
        """Check if the card is expired and update is_active accordingly."""
        if timezone.now().date() > self.expiry_date:
            self.is_active = False
        else:
            self.is_active = True

    def can_scan(self):
        """Check if the card can be scanned (maximum twice per day)."""
        current_date = timezone.now().date()
        
        # Reset the daily scan count if the last scan was on a different day
        if self.last_scan_date != current_date:
            self.daily_scan_count = 0
            self.last_scan_date = current_date

        # Allow scanning if the daily scan count is less than 2
        return self.daily_scan_count < 2

    def register_scan(self):
        """Register a scan if the card can be scanned."""
        if self.can_scan():
            self.daily_scan_count += 1
            self.last_scan_date = timezone.now().date()
            self.save()
        else:
            raise ValueError("This card has reached the maximum number of scans for today.")

class ScanDevice(models.Model):
    device_name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50, choices=[('NFC Reader', 'NFC Reader'), ('RFID Reader', 'RFID Reader')])
    serial_number = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.device_name} ({self.device_type})'
    
class CardScan(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , related_name='users')
    location = models.CharField(max_length=255)
    scan_date = models.DateTimeField(auto_now_add=True)
    scan_result = models.TextField()
    status = models.CharField(max_length=50, choices=[('Success', 'Success'), ('Failed', 'Failed')])

    def __str__(self):
        return f'Scan at {self.location} on {self.scan_date}'

    def save(self, *args, **kwargs):
        today = timezone.now().date()
        scans_today = CardScan.objects.filter(card=self.card, scan_date__date=today).count()

        if scans_today >= 2:
            raise ValidationError("This card has already been scanned twice today.")

        super().save(*args, **kwargs)

class ScanLog(models.Model):
    scan = models.ForeignKey(CardScan, on_delete=models.CASCADE)
    log_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    log_type = models.CharField(max_length=50, choices=[('INFO', 'INFO'), ('WARNING', 'WARNING'), ('ERROR', 'ERROR')])

    def __str__(self):
        return f'Log for {self.scan} at {self.log_time}'

class AccessControl(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    access_location = models.CharField(max_length=255)
    access_time = models.TimeField()
    is_granted = models.BooleanField(default=True)

    def __str__(self):
        return f'Access {"granted" if self.is_granted else "denied"} for {self.card}'
