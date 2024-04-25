from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from .forms import postForm

# Create your views here.
def home(request):
    form = postForm
    context = {
        "posts" : post.objects.all(),
        "form": form
    }
    if request.method == "POST":
        if form.is_valid :
            form = postForm(request.POST)
            form.user = request.user
            form.title = request.POST.get('title')
            form.content = request.POST.get('content')
            form.save()
    return render(request, "index.html", context)