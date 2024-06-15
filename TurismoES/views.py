from django.shortcuts import render
from .models import Service
# Create your views here.


def index(request):
    context={}
    return render(request, 'turismo/index.html', context)


def service_list(request):
    services = Service.objects.all()
    return render(request, 'turismo/service_list.html', {'services': services})
