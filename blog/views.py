from django.shortcuts import render
from .models import POST
from django.utils import timezone

def post_list(request):
	posts = POST.objects.filter()
	return render(request, 'blog/post_list.html', {'posts': posts})