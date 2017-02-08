from django.shortcuts import render

from .models import Post


def post_list(request):
    context = {'post_title': Post.objects.order_by('-published_date')}
    print(context)
    return render(request, 'blog/index.html', context)
