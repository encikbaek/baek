from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(name=name, email=email, message=message)

        contact.save()

        message.success(request, "Thanks for your enquiry, we'll be in touch shortly.")

        return redirect('/')