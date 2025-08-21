from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings



def index(request):
    success = request.GET.get('success', False)
    return render(request, 'index.html', {'success': success})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database (optional)
        Contact.objects.create(name=name, email=email, message=message)

        # Compose email content
        subject = f"New Contact Form Submission from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['your_email_box@example.com']  # Replace with your email where you want to receive messages

        # Send email
        send_mail(subject, message_body, from_email, recipient_list)

        # Redirect with success flag
        return redirect('/?success=1')

    return render(request, 'contact.html')
