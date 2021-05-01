from django.urls import path
from django.contrib import admin
from .views import UserPostListView,PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,AddCommentView
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(),name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(),name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name="post-delete"),
    path('post/new/', PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/comment', AddCommentView.as_view(),name="add_comment"),
    path('about/', views.about,name="blog-about"),
    path('search/', views.search,name="blog-search"),
]
