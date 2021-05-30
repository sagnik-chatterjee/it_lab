from q1.models import Page
from django.shortcuts import render

# Create your views here.

from .forms import PageForm, CategoryForm
from .models import Page, Category


def page1(request):
    form = PageForm()
    obj = Page.objects.get(id=1)
    if request.method == "POST":
        print(request.POST)
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form, "objects": obj}
    return render(request, "q1/page1.html", context)


def page2(request):
    form = CategoryForm()
    obj = Category.objects.get(id=1)
    if request.method == "POST":
        print(request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form, "objects2": obj}
    return render(request, "q1/page2.html", context)
