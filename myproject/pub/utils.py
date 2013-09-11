from django.conf import settings
from django.core.mail import mail_managers
from django.template import Template, Context
from django.template.loader import get_template


def send_order_email(data):
    managers_emails = [it[1] for it in settings.MANAGERS]
    template = get_template("request_email.html") #Template()
    body = template.render(Context(data))
    mail_managers("Delikat-Cake: New Order", body, fail_silently=False, html_message=body)
