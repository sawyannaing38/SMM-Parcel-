from django.db import models

# Create your models here.
class Parcel(models.Model):
    sender = models.TextField(max_length=64)
    name = models.TextField(max_length=64)
    phone = models.TextField(max_length=11)
    item = models.TextField(max_length=64)
    count = models.IntegerField()
    cost = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[("pick", "Pick"), ("unpick", "Unpick"), ("busy", "Busy"), ("unconnect", "Unconnect")]
    )
    taken = models.BooleanField(default=False)
    receiveDate = models.DateField()