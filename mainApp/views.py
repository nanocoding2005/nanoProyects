from django.shortcuts import render
from .models import proyectlist 

def DatabaseQuery(request):
    proyects = proyectlist.objects.all().order_by('-id')
    return render(request, 'index/index.html', {'proyects':proyects})
    