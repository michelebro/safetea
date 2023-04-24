from django.urls import path
from . import views
from .views import add_post, login_view, delete_post


urlpatterns= [
    path('', views.home),
    path('about/', views.about),
    path('posts/', views.post_list),
    path('add_post/', add_post, name='add_post'),
    path('login/', login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
    path('add-comment/<int:post_id>/', views.add_comment, name='add_comment'),
]