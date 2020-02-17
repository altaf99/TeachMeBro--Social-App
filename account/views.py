from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import login, authenticate
from . import forms

# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
    
        return render(request, "registration/index.html")

def signup(request):
    if request.method == 'POST':
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('index')
    else:
        form = forms.UserCreateForm()
    return render(request, 'registration/signup.html', {'form': form})