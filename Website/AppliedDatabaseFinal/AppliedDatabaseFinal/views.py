from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    """
    View for the home page of the Django application.
    """
    return render(request, 'EnergyWebsite/templates/home.html')