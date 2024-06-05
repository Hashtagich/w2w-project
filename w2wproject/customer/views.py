from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import viewsets
from .models.customer import Customer
from .serializers import CustomerSerializer
from django.http import JsonResponse
from django.views import View
from django.urls import reverse
from django.conf import settings
import requests





@login_required
def profile_view(request):
    return render(request, 'profile.html', {'customer': request.user})

def home_view(request):
    return render(request, 'home.html')



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer






class CustomConfirmEmailView(View):
    def get(self, request, key, *args, **kwargs):
        url = request.build_absolute_uri(reverse('account_email_verification_sent'))
        data = {'key': key}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return JsonResponse({'message': 'Email confirmed!'}, status=200)
        return JsonResponse({'message': 'Email confirmation failed.'}, status=400)
