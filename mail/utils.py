import time
from django.template import Context, Template
from django.core.mail import EmailMultiAlternatives

from .models import Subscriber
from mailganer import settings


def sent_mailing(subscriber_pk):
    subscriber = Subscriber.objects.get(id=subscriber_pk)
    template = Template(subscriber.mailing_id.content)
    
    data = {
        "firstname": subscriber.firstname,
        "lastname": subscriber.lastname,
        "birthday": subscriber.birthday
    }
    context = Context(data)
    content = template.render(context)

    msg = EmailMultiAlternatives(subscriber.mailing_id.title, content, settings.EMAIL_HOST_USER, [subscriber.email])
    msg.attach_alternative(content, "text/html")
    msg.send()

    time.sleep(1)
