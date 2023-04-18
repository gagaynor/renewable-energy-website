from django.shortcuts import render

def home(request):
    """
    View for the home page of the Django application.
    """
    return render(request, 'home.html')

def about(request):
    """
    View for the about page of the Django application.
    """
    return render(request, 'about.html')
