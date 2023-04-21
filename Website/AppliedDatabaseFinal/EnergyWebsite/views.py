from django.shortcuts import render
import pandas
from django.views.generic import ListView
from .forms import Filters

def home(request):
    """
    View for the home page of the Django application.
    """
    filters = Filters(request.POST or None)
    context = {
        'filters': filters
    }

    return render(request, 'home.html', context)

def about(request):
    """
    View for the about page of the Django application.
    """
    return render(request, 'about.html')
