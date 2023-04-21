import pandas
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib import messages
from .forms import Filters
from .models import *
# Create your views here.
from .utils import get_chart

def load(request):
    
    filter_selections = Filters(request.POST or None)

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        time_frequency = request.POST.get('time_frequency')
        load = request.POST.get('load')
        