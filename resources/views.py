from django.shortcuts import render
from resources.models import Post
# Create your views here.

def blog_index(request):

    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
        }
    return render(request, "blog_index.html", context)

