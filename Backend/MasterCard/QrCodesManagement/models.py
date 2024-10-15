import random
from django.db import models
from django.utils import timezone
from userManagement.models import CustomUser
from CardScanning.models import Card

class QRCode(models.Model):
    code_value = models.IntegerField(unique=True, null=True, blank=True)  # Random value between 0 and 16
    created_at = models.DateTimeField(auto_now_add=True)
    associated_card = models.OneToOneField(Card, on_delete=models.CASCADE)  # One QR code per card
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # One QR code per user

    def __str__(self):
        return f'QR Code: {self.code_value}'

    def save(self, *args, **kwargs):
        # Generate a random code_value if not already set
        if self.code_value is None:
            self.code_value = random.randint(0, 16)

        # Ensure unique code_value
        while QRCode.objects.filter(code_value=self.code_value).exists():
            self.code_value = random.randint(0, 16)

        super().save(*args, **kwargs)


class QRScan(models.Model):
    qr_code = models.ForeignKey(QRCode, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    scan_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Scan of {self.qr_code} by {self.user} on {self.scan_date}'

    class Meta:
        ordering = ['-scan_date']

    def save(self, *args, **kwargs):
        # Check if user is admin
        if not self.user.is_staff:
            raise ValueError("Only admin users can scan QR codes.")
        
        # Check if the associated card is expired
        self.qr_code.associated_card.check_expiry()
        if not self.qr_code.associated_card.is_active:
            raise ValueError("Cannot scan QR code: The associated card is expired.")

        super().save(*args, **kwargs)