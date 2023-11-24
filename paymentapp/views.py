from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Payment_service
from medical.userapp.models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponsePermanentRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.mail import send_mail
from medical.serviceapp.models import Book_service
from .models import Payment_service



@login_required
def bookingPayment(request, book_id):
    pass


@login_required
def failPayment(request, book_id):
    messages.error(request, ('Your payment Fails!'))

    return HttpResponsePermanentRedirect(reverse('patient_booking', args=(request.user.id, )))

@login_required
def successPayment(request, book_id):
    booking = Book_service.objects.get(booking_id=book_id)

    payment = Payment_service(user_id = request.user.id, booking_id = book_id, amount = booking.price)
    payment.save()

    payment = Book_service.objects.filter(booking_id=book_id).update(payment=True)

    send_mail(
            'Payment Confirmed',
            f'Dear Dr. {booking.hod.first_name}, Your booking has been approved. see your booking details for more information or click',
            'techcare@gmail.com',
            [booking.hod.email],
            fail_silently=False,
        )

    messages.success(request, ('Your payment was successful'))
    return HttpResponsePermanentRedirect(reverse('patient_booking', args=(request.user.id, )))
