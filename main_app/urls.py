from django.urls import path
from . import views
from .views import add_post, login_view, delete_post


urlpatterns= [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.post_list, name= 'posts'),
    path('add_post/', add_post, name='add_post'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('add-comment/<int:post_id>/', views.add_comment, name='add_comment'),
]