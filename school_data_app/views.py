from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView

from .models import School

class SchoolDataParseView(ListView):
    """
     Slouží pro zobrazení dat škol.
    """
    context_object_name = 'schools'
    template_name = 'list_schools.html'

    def get_queryset(self):
        # Když je zadaný query_param 'number' vrátí tolik škol kolik je v number
        if 'number' in self.request.GET:
            number = int(self.request.GET.get('number'))
            queryset = School.objects.all()[:number]
        else:
            queryset = School.objects.all()[:10]

        return queryset
