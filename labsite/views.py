from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'index.html')
def showpost(request):
    posts = Post.objects.all()
    
    return render(request, 'post.html',{"posts": posts})    