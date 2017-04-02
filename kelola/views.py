from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

#from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'kelola/post_list.html', {'posts': posts})
   # post = get_object_or_404(Post, pk = pk)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'kelola/post_detail.html', {'post': post})

'''def post_new(request):
    form = PostForm()
    return render(request, 'kelola/post_edit.html', {'form': form})
# Create your views here.
'''