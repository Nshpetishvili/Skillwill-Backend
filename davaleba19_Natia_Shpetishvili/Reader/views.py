from django.shortcuts import render

# Create your views here.
from .models import Reader

def reader_profile(request):
    if request.method == 'POST':
        # Handle form submission here
        # Save reader data to the database
        pass
    return render(request, 'reader_profile.html')