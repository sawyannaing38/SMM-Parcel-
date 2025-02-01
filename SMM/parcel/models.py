from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Parcel(models.Model):
    sender = models.TextField(max_length=64)
    name = models.TextField(max_length=64)
    phone = PhoneNumberField(region="MM")
    item = models.TextField(max_length=64)
    count = models.IntegerField()
    cost = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[("pick", "Pick"), ("unpick", "Unpick"), ("busy", "Busy"), ("unconnect", "Unconnect")]
    )
    taken = models.BooleanField(default=False)
    receiveDate = models.DateField()

# Model for Taker
class Taker(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)
    parcel = models.OneToOneField(Parcel, on_delete=models.CASCADE, related_name="taker")
    takenTime = models.DateTimeField()