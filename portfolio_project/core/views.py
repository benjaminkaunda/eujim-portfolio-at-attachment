import certifi
import ssl
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import ContactForm
import re
import ssl

# CRITICAL: Disable SSL verification at module level (before any functions)
ssl._create_default_https_context = ssl._create_unverified_context


def home(request):
    context = {
        'name': 'Benjamin Kaunda',
        'title': 'Computer Science Student | Full-Stack Web Developer',
        'university': 'Karatina University',
    }
    return render(request, 'core/index.html', context)


def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Sanitize inputs
            name = re.sub(r'[\r\n\t]', ' ', name).strip()
            email = re.sub(r'[\r\n\t]', '', email).strip()
            
            # Static subject (no variables)
            subject = 'New Portfolio Contact'
            
            # Clean body
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            # Use only email address
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['benjaminkaunda095@gmail.com']

            try:
                send_mail(
                    subject=subject,
                    message=body,
                    from_email=from_email,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
                messages.success(request, "Thank you! Your message has been sent successfully.")
                return redirect('home')
                
            except BadHeaderError as e:
                print(f"BadHeaderError {str(e)}")
                messages.error(request, f"Email error: {str(e)}")
                return redirect('home')
                
            except Exception as e:
                print(f"Email Error: {str(e)}")
                messages.error(request, f"Error: {str(e)}")
                return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    return redirect('home')