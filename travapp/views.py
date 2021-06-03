from django.shortcuts import render
from .models import val


def index(request):
    vals = val.objects.all()
    return render(request, 'travapp\\index.html', {'vals': vals})
