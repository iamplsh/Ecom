from django import forms
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name',max_length = 100)
    message = forms.CharField(max_length=600,widget=forms.Textarea)


    def send_mail(self):
        # logger.info("Sending mail to customer service")
        message = "From: {0} \n {1}".format(self.cleaned_data["name"],self.cleaned_data["message"],)
        send_mail(
            "Test Message",
            message,
            "site@booktime.domain",
            ["iamplsh516@gmail.com"],
            fail_silently=False,
        )
