from celery import shared_task
import time
from django.core.mail import send_mail
from typing import List
from core import settings

@shared_task
def handle_time_sleep():
    print('starting sleep')
    time.sleep(10)
    print("sleeping complete")

@shared_task(bind=True)
def custom_send_email(self):
    try:
        print('sending mails')
        send_mail(subject='hello', message='msg', from_email=settings.EMAIL_HOST_USER, recipient_list=[settings.EMAIL_HOST_USER],
                                                fail_silently=False)
        print("done")
    except Exception as e:
        print('err', str(e))
        