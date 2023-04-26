from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from main_app.forms import PostForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, PostForm, CommentForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
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
                return redirect('about')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid() and form.cleaned_data['gender'] == 'F' and form.cleaned_data['age'] >= 13:
            user = form.save()
            login(request, user)
            return redirect('about')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request, 'posts/index.html', {'post': post})

@login_required
def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment was added successfully!')
            return JsonResponse({
                'success': True,
                'comment_html': render_to_string('posts/comment.html', {'comment': comment})
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = CommentForm()
    return render(request, 'posts/index.html', {'form': form, 'post': post})


def logout_view(request):
    logout(request)
    return redirect('login')




