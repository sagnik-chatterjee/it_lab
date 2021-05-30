from django.shortcuts import render, redirect
from .forms import BasicForm


def index(request):
    form = BasicForm()
    return render(request, 'q2/firstPage.html', {'form': form})


def first_page(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll = form.cleaned_data['roll']
            subject = form.cleaned_data['subject']
        
        request.session['name'] = name
        request.session['roll'] = roll
        request.session['subject'] = subject

    return redirect('/q2/secondPage')

def second_page(request):
    name = request.session['name']
    roll = request.session['roll']
    subject = request.session['subject']

    context = {'name': name, 'roll': roll, 'subject': subject}
    return render(request, 'q2/secondPage.html', context)