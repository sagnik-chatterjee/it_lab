from django.shortcuts import render

# Create your views here.
from .forms import ProductInfoForm
from .models import ProductInfo


def index(request):
    form = ProductInfoForm()
    obj = ProductInfo.objects.get(id=2)
    if request.method == "POST":
        print(request.POST)  ##helpful for logging the info
        form = ProductInfoForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form,"object": obj}

    return render(request, "q4/index.html", context)
