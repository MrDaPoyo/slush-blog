from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from .forms import postForm

# Create your views here.
def home(request):
    form = postForm
    context = {
        "posts":post.objects.all(),
        "form":form
    }
    form = postForm()
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.author = request.user
            thread.title = form.cleaned_data["title"]
            thread.content = form.cleaned_data["content"]
            thread.save()
    return render(request, "index.html", context)