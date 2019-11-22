from django.shortcuts import render
from . import models
from django.views import View


#def home(request):
#    """
#    The Blog homepage
#    """
#    return render(request, 'blog/home.html', {'message': 'MITRA WORLD!'})

def home(request):
    # Get last 3 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:10]
    # Add as context variable "latest_posts"
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/home.html', context)
