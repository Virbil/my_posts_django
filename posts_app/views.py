from django.shortcuts import redirect, render
from .models import *

def posts(request):
    context = {
        "all_posts": Post.objects.all()
    }
    return render(request, "index.html", context)

def add_post(request):
    Post.objects.create(
        content = request.POST["content"]
    )   
    return redirect('/')