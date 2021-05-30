from django.shortcuts import render, redirect
from .forms import BasicForm


def index(request):
    form = BasicForm()
    return render(request, 'q3/register.html', {'form': form})

def register(request):
    username=""
    password=""
    email=""
    contact=""
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']

        context = {'username': username, 'password': password, 'email': email, 'contact': contact}
    return render(request, 'q3/success.html', context)

