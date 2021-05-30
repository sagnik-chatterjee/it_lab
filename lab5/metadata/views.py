from django.shortcuts import render

# Create your views here.
def metadata(request):
    return render(request, 'metadata/index.html')