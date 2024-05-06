from django.shortcuts import render

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the sender's email account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Close the connection
    server.quit()

# Create your views here.
def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def courses(request):
    return render(request,"courses.html")


def services(request):
    return render(request,"services.html")


def pricing(request):
    return render(request,"pricing.html")


def gallery(request):
    return render(request,"gallery.html")


def contact(request):
    sent = False
    if request.method == "POST":
        try:
            message = request.POST.get("message")
            name = request.POST.get("name")
            number = request.POST.get("number")
            subject = request.POST.get("subject")
            sender_email = 'vediccomputer51@gmail.com'
            sender_password = 'buknewxfyfchumlq'
            recipient_email = 'atulg0736@gmail.com'
            message = f'Hey admin, {name} with contact number {number} has requested a querry: {message}'
            send_email(sender_email, sender_password, recipient_email, subject, message)
            sent = True
        except:
            pass
    context = {
        'sent':sent,
    }
    return render(request,"contact.html",context)
