from django import forms
from main_app.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'city', 'age', 'description')

class CustomUserCreationForm(UserCreationForm):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    age = forms.IntegerField(min_value=13, help_text="You must be at least 13 years old to sign up.")
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('gender', 'age', 'first_name', 'last_name',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'text')
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }