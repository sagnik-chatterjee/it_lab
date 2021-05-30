from django.shortcuts import render, redirect
from .forms import BasicForm

prices = {
    'HP': {'mobile': 5000, 'laptop': 15000},
    'Nokia': {'mobile': 6000, 'laptop': 16000},
    'Samsung': {'mobile': 7000, 'laptop': 17000},
    'Motorolla': {'mobile': 8000, 'laptop': 18000},
    'Apple': {'mobile': 9000, 'laptop': 19000},
}

def index(request):
    form = BasicForm()
    return render(request, 'q4/first_page.html', {'form': form})

def produce_bill(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            mobile = form.cleaned_data['mobile']
            laptop = form.cleaned_data['laptop']
            quantity = form.cleaned_data['quantity']

            total_bill = 0

            if (mobile):
                total_bill = total_bill + prices[company]['mobile']
            if (laptop):
                total_bill = total_bill + prices[company]['laptop']


            context = {'company': company, 'mobile': mobile, 'laptop': laptop, 'quantity': quantity, 'total_bill': total_bill}
        else:
            context = {}
    return render(request, 'q4/second_page.html', context)


