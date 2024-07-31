from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
import time
from .tasks import handle_time_sleep, custom_send_email
from django.shortcuts import render

# Create your views here.
class HomeAPI(APIView):
    def get(self, request, *args, **kwargs):
        # handle_time_sleep.delay()
        custom_send_email.delay()
        data = {'data': 'wassup', 'check_it_out': 'checkeddd'}
        return render(request, 'base.html', data)
    