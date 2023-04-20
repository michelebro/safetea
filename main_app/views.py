from django.shortcuts import render

class Post:
    def __init__(self, name, city, description, age):
        self.name = name
        self.city = city
        self.description = description
        self.age = age

post = [
    Post('man', 'siamese', 'loud', '35'),
    Post('man1', 'siamese', 'loud', '44'),
    Post('man2', 'siamese', 'loud', '18')
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def post(request):
    return render(request, 'posts/index.html', {'posts': post})