from django.conf import settings
import django.contrib
from django.core.mail import send_mail



def send_account_activation_email(email, email_token):
    subject = 'Your account need to be verified'
    #email_from = settings.EMAIL_HOST_USER
    email_from = 'f2018065077@gmail.com'
    messages = f'Hi Click on the link to activiate your account http://localhost:8000/accounts/activate/{email_token} '
    send_mail(subject, messages, email_from, [email])