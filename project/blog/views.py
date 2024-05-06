from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import post
from .forms import postForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request, id=1):
    form = postForm
    Post = post.objects.get(pk=id)
    context = {
        "posts":post.objects.all().order_by('-id'),
        "form":form,
        "post":Post,
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

def view(request, id):
    Post = post.objects.get(pk=id)
    context = {
        "post":Post,
    }
    return render(request, "view.html", context)

def homeRedirect(request):
    return redirect("../home/1")

@login_required
def deletePost(request, id):
    Post = post.objects.get(pk=id)
    Post.delete()
    return redirect("home")