from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'dashboard/index.html')
@login_required()
def profile(request):
    return render(request, 'dashboard/profile.html')

# Create your views here.
