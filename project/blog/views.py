from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from .forms import postForm

# Create your views here.
def home(request):
    context = {
        "posts" : post.objects.all(),
        "form": postForm
    }
    return render(request, "index.html", context)