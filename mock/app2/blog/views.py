from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import BlogPost, BlogPostForm


def archive(request):
    posts = BlogPost.objects.all()[:10]  # retruve the last 10 new posts
    return render(request, "archive.html", {"posts": posts, "form": BlogPostForm()})

def create_blogpost(request):
    if request.method == "POST":
        form  = BlogPostForm(request.POST)
        if form.is_valid():
            #saves into db the timestamp 
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/') #go back to this page 
