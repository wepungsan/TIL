from django.shortcuts import render

from posts.models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}

    return render(request, 'posts/post_list.html', context=context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post':post}

    return render(request, 'posts/post_detail.html', context=context)
