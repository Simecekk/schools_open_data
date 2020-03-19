from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView

from .models import School

class SchoolDataParseView(ListView):
    """
     Zobrazuje prvních 10 škol z DB
    """
    queryset = School.objects.all()[:10]
    context_object_name = 'schools'
    template_name = 'list_schools.html'

