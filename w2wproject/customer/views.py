from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer


@login_required
def profile_view(request):
    return render(request, 'profile.html', {'customer': request.user})

def home_view(request):
    return render(request, 'home.html')




class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
