from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Post, Responses, Newsletters


class PostList(ListView):
    model = Post
    ordering = '-created'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
