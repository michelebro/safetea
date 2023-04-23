from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from main_app.forms import PostForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, PostForm

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
            return redirect('/posts/')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})

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
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid() and form.cleaned_data['gender'] == 'F' and form.cleaned_data['age'] >= 13:
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts/index.html')
    return render(request, 'posts/index.html', {'post': post})