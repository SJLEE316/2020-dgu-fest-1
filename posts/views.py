from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def gallery(request):
    posts=Post.objects.all()
    return render(request, 'posts/gallery.html', {'posts':posts})

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    if request.method == "POST":
        category = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')
        mediafile = request.FILES.get('mediafile')
        mediatype = mediafile.content_type
        Post.objects.create(category=category, title=title, content=content, mediafile=mediafile, mediatype=mediatype)
    return redirect('posts:gallery')


def update(request, id):
    post = Post.objects.get(pk=id)
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.mediafile = request.FILES.get("mediafile")
        post.save()
        return redirect('posts:gallery')
    return render(request, 'posts/update.html', {"post":post})




