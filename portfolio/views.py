from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from datetime import datetime

from .models import EmailForm
from .forms import SendEmailForm


def home(request):
    return render(request, "index.html")


def contact(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)

        if form.is_valid():
            sender_name = form.cleaned_data["sender_name"]
            sender_email = form.cleaned_data["sender_email"]
            date_sent = datetime.now()
            message = form.cleaned_data["message"]

            EmailForm.objects.create(sender_name=sender_name,
                                     sender_email=sender_email,
                                     date_sent=date_sent,
                                     message=message)

            message_subject = f"Message received from {sender_name} ({sender_email})"
            email_message = EmailMessage(subject=message_subject,
                                         body=message,
                                         to=[settings.EMAIL_HOST_USER])
            email_message.send()
        else:
            print(form.errors)

    return render(request, "contact.html")
