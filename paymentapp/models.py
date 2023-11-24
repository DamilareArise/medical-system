from django.db import models
from medical.userapp.models import Profile
from medical.serviceapp.models import Book_service

# Create your models here.
class Payment_service(models.Model):

    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, null=False, unique=False, on_delete=models.CASCADE )
    booking = models.ForeignKey(Book_service, null=False, unique=False, on_delete=models.CASCADE )
    amount = models.BigIntegerField(unique=False, null= False)
    date_of_payment = models.DateTimeField(auto_now_add=True, null=False)
    paystack_detail = models.BigIntegerField(unique=True, null=False)