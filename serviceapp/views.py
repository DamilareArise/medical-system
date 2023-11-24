from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from medical.userapp.models import Profile
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect
from django.db.models import Q
from django.core.mail import send_mail



def homepage_service(request):
    services = Services.objects.all()
    services1 = services[0:2]
    services2 = services[2:4]
    
    return render (request, 'serviceapp/service.html', {'services1':services1,'services2':services2 })

@login_required
def  displayService(request):

    services = Services.objects.all()

    return render (request, 'serviceapp/display_service.html', {'services':services})


@login_required
def  viewService(request, serv_id):

    services = Services.objects.all().filter(service_id = serv_id)

    return render (request, 'serviceapp/view_service.html', {'services':services})

@login_required
def  createService(request):
    if request.method == "POST":
        service_form = Service_form(request.POST, request.FILES )
        if service_form.is_valid():
            service_form.save()
        return homepage_service(request)
    else:
        service_form = Service_form()
        return render(request, 'serviceapp/create_service.html', {'serviceForm': service_form})

@login_required
def edit_service(request, serv_id):
    service = get_object_or_404(Services, service_id=serv_id)
    
    if request.method == "POST":
        
        serv_form = Service_form(request.POST, instance=service)
        
        if  serv_form.is_valid():
            serv_form.save()
           
            messages.success(request, 'Service successfully updated!')
            return displayService(request)
        else:
        #     print("invalid invalid")
            messages.error(request, 'Please correct the error below.')
            return HttpResponsePermanentRedirect(reverse('edit_service', args=(serv_id,)))
    else:
        serv_form = Service_form(instance=service)
        return render(request, 'serviceapp/edit_service.html', {'serv_form': serv_form})


@login_required
def deleteService(request, serv_id):
    try:
        Services.objects.get(service_id = serv_id).delete()
        messages.info(request, 'Service deleted successfully')
    except:
        messages.error(request, 'Something went wrong')
        return HttpResponsePermanentRedirect(reverse('edit_service', args=(serv_id,)))

    return redirect('display_service')


@login_required
def booking_record(request, userid):
    
    if request.user.is_superuser:
        services = Book_service.objects.all()
    elif request.user.is_staff:
        services = Book_service.objects.all().filter(hod = userid)
    else:
        services = Book_service.objects.all().filter(user_id = userid)

    return render (request, 'serviceapp/booking_record.html', {'services':services})


@login_required
def book_service(request, serv_id):
    service = Services.objects.get(service_id = serv_id)
    print(service)
    if request.method == "POST":
        booking_form = BookService_form(request.POST)
        if booking_form.is_valid():
            form = booking_form.save(commit=False)
            form.user_id = request.user.id
            form.hod_id = service.HoD.id
            form.service = service
            form.service_name = service.service_option
            form.price = service.price

            form.save()

        return HttpResponsePermanentRedirect(reverse('booking_record', args=(request.user.id,)))
    else:
        service_form = BookService_form()

        return render(request=request, template_name='serviceapp/booking_details.html', context={"serviceForm": service_form})


