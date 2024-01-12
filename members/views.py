from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.template import loader


def ShowInfo(request):
    member=models.listmember.objects.all().order_by('name')
    arg={'myvar':member}
    return render(request,'index.html',arg)

# Create your views here.
