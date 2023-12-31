from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Services(models.Model):
    dept = [
        ("Emergency", "Emergency"),
        ("Operation & Surgery", "Operation & Surgery"),
        ("Outdoor Checkup", "Outdoor Checkup"),
        ("Ambulance Service", "Ambulance Service"),
        ("Medicine & Pharmacy", "Medicine & Pharmacy"),
        ("Medical Lab","Medical Lab")
    ]

    service = [
        ('Cosmetic Dentistry', 'Cosmetic Dentistry'),
        ('Dental Implant', 'Dental Implant'),
        ('Dental Bridges', 'Dental Bridges'),
        ('Teeth Whitening', 'Teeth Whitening')
    ]

    status = [
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Declined', 'Declined')
    ]


    service_id = models.AutoField(primary_key=True)
    service_option = models.CharField(choices=service, max_length=20, null=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    HoD = models.OneToOneField(User, on_delete=models.CASCADE, unique= True)
    service_logo = models.ImageField(upload_to='service_logo/', blank=True, null=True, unique=False)
    price = models.BigIntegerField(unique=False)
    description = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'SERV-0{self.service_id}-{self.service_option}'
    



class Book_service(models.Model):

    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, blank=False, unique=False, on_delete=models.CASCADE)
    hod = models.ForeignKey(User, related_name="hod", null=False, blank=False, unique=False, on_delete=models.CASCADE, default=1)
    service = models.ForeignKey(Services, null=False, blank=False, unique=False, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100, blank=True, null=True, unique=False)
    date_created = models.DateField(auto_now_add=True)
    payment = models.BooleanField(default=False, blank=True, null=True, unique=False)
    price = models.BigIntegerField(unique=False, default=00)

    
    def __str__(self):
        return f'BOOK-0{self.booking_id}-{self.user.first_name}'