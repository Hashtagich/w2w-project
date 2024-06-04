from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import viewsets
from .models.customer import Customer
from .serializers import CustomerSerializer



@login_required
def profile_view(request):
    return render(request, 'profile.html', {'customer': request.user})

def home_view(request):
    return render(request, 'home.html')



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
