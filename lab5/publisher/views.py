from django.shortcuts import render

# Create your views here.
def publisher(request):
    return render(request, 'publisher/index.html'