from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import smtplib

from email.mime.text import MIMEText



class ContactForm(forms.Form):

    to_username = forms.CharField(max_length=120)
    to_email = forms.EmailField()
    subject = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('to_username').strip()
        to_email = cl_data.get('to_email')
        subject = cl_data.get('subject')

        msg = f'Hi..{name} '
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg ,to_email

    def send(self):

        subject, msg ,to_email= self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            html_message = render_to_string('contact/mail_template.html',context={'message':msg}),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email]
        )
        


