from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Card )
admin.site.register(CardScan)
admin.site.register(AccessControl) 
admin.site.register(ScanDevice) 
admin.site.register(ScanLog)
