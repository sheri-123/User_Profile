# web/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Contact
import json

def index(request): # RENAMED to index
    if request.method == 'POST':
        try:
            # Decode the request body
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            service = data.get('service')
            message = data.get('message')

            # Basic validation
            if not all([name, email, service, message]):
                return JsonResponse({'success': False, 'error': 'All fields are required.'}, status=400)

            # Create and save the contact object
            contact = Contact.objects.create(
                name=name,
                email=email,
                service=service,
                message=message
            )

            # Send an email notification
            send_mail(
                f'New Portfolio Contact: {service} request from {name}', # Subject
                f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}', # Message
                'muhammadshaheryar1920@gmail.com', # From email
                ['muhammadshaheryar1920@gmail.com'], # To email
                fail_silently=False,
            )

            return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    # For a GET request, render index.html
    return render(request, 'index.html') # CORRECTED to index.html