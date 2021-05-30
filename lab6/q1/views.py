from django.shortcuts import render
from .forms import BasicForm


def index(request):
    form = BasicForm()
    return render(request, 'q1/index.html', {'form': form})

def result(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            car_manufacturer = form.cleaned_data['car_manufacturer']
            model_name = form.cleaned_data['model_name']
    
    context = {'car_manufacturer': car_manufacturer, 'model_name': model_name}
    return render(request, 'q1/result.html', context)

