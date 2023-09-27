from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author, Post, Responses
from .filters import PostFilter
from .forms import CreateForm, FormResponses
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.contrib.auth.models import User


class PostList(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Post
    ordering = '-created'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class Search(PostList):
    raise_exception = True
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 5


class PostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = CreateForm
    model = Post
    template_name = 'create_post.html'

    def form_valid(self, form):
        user = self.request.user
        if Author.objects.filter(author=user):
            form.instance.author = Author.objects.get(author=user)
        else:
            person = Author.objects.create(author=user)
            person.save()
            form.instance.author = person

        return super().form_valid(form)


class UserResponses(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Responses
    ordering = '-date_created'
    template_name = 'responses.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        responses = Responses.objects.filter(re_post__author__author=self.request.user)
        context["responses"] = responses
        return context


def create_responses(request, id, form=None):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        form = FormResponses(request.POST)
        form.instance.re_post = post
        form.instance.re_user = User.objects.get(id=request.user.id)
        if form.is_valid():
            form.save()

    return render(request, 'create_responses.html', {'form': form})


class UpdatePost(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = CreateForm
    model = Post
    template_name = 'create_post.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class MyPosts(ListView):
    model = Post
    ordering = '-created'
    template_name = 'posts_author.html'
    context_object_name = 'mypost'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(author__author=self.request.user)
        context['myposts'] = posts
        return context


