from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login
import requests
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from livestream_signs.forms import CreateUserForm

# Create your views here.
def stream(request):
    return render(request, 'stream.html', {'room_name': "Signs"})


class VideoStreamView(TemplateView):
    template_name = "stream.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            # Make an HTTP request to the Node.js video streaming endpoint
            video_url = "http://localhost:3000/video"  # Update with the actual Node.js server URL and endpoint
            response = requests.get(video_url)

            # Check if the request was successful
            if response.status_code == 200:
                context['video_url'] = video_url
            else:
                context['video_url'] = None  # Handle the case where the request was not successful
        except requests.exceptions.RequestException as e:
            context['video_url'] = None  # Handle request exceptions, e.g., connection error

        return context


def signup(request):
    form = CreateUserForm()
        
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' +user)
            
            return redirect('userlogin')
    
    context = {'form':form}
    
    return render(request, 'signup.html', context)

    
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('stream')
        else:
            messages.info(request, 'Username or password is incorrect')
            
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('userlogin')