from operator import index
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Datas
from .models import Appointment
from datetime import datetime
from django.db import IntegrityError

# Create your views here.

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def Department(request):
    return render(request,'Department.html')

def Doctors(request):
    return render(request,'Doctors.html')


    
def contact(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        name = request.POST.get('name', '')
        mail = request.POST.get('mail', '')
        number = request.POST.get('number', '')
        
        if message and name and mail and number:
            
            Datas.objects.create(
                message=message,
                name=name,
                mail=mail,
                number=number
            )
            return redirect('success')
    
    return render(request, 'contact.html')

    

def blog(request):
    return render(request,'blog.html')
    
    
def book_appointment(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        date = request.POST.get('datepicker')
        department = request.POST.get('departmentselect')
        doctor = request.POST.get('doctorselect')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Check if date is provided
        if date:
            try:
                # Save form data to the database using the Appointment model
                appointment = Appointment.objects.create(
                    date=date,
                    department=department,
                    doctor=doctor,
                    name=name,
                    phone=phone,
                    email=email
                )

                # Optionally, you can redirect to a success page
                return redirect('success')  # Replace 'success' with the name of your success URL pattern

            except IntegrityError as e:
                # Handle IntegrityError (e.g., duplicate entry)
                return render(request, 'index.html', {'error_message': 'IntegrityError: ' + str(e)})

        else:
            # If date is not provided, render the form again with an error message
            return render(request, 'index.html', {'error_message': 'Date is required'})

    # If the request method is not POST, render the initial form
    return render(request, 'index.html')    

def success(request):
    return render(request,'success.html')
    
    
    