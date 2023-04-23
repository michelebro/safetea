from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from main_app.forms import PostForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts/index.html')
    else:
        form = PostForm()
    return render(request, 'main_app/add_post.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home.html')
        else:
            print(form.errors)
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form, 
        'error': error_message 
    })

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('delete_post')
    return render(request, 'posts/delete_post.html', {'post': post})